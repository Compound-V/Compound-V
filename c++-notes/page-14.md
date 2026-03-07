# Page 14

```markdown
# Shadow API Inspector
## Complete Documentation - From Zero to Mastery

**Version:** 1.0.0  
**Last Updated:** November 2024  
**License:** MIT

---

# Table of Contents

1. [Introduction](#1-introduction)
   - [What is Shadow API Inspector?](#11-what-is-shadow-api-inspector)
   - [Why Was It Built?](#12-why-was-it-built)
   - [Who Is It For?](#13-who-is-it-for)
   - [Key Features Overview](#14-key-features-overview)

2. [The Problem Space](#2-the-problem-space)
   - [Third-Party API Blindness](#21-third-party-api-blindness)
   - [Client-Side Data Leakage](#22-client-side-data-leakage)
   - [Supply Chain Attacks](#23-supply-chain-attacks)
   - [Shadow APIs](#24-shadow-apis)
   - [Real-Time Context Loss](#25-real-time-context-loss)

3. [Architecture Deep Dive](#3-architecture-deep-dive)
   - [High-Level Overview](#31-high-level-overview)
   - [File Structure](#32-file-structure)
   - [Component Breakdown](#33-component-breakdown)
   - [Data Flow](#34-data-flow)
   - [Cross-Browser Compatibility](#35-cross-browser-compatibility)

4. [Installation Guide](#4-installation-guide)
   - [Requirements](#41-requirements)
   - [Chrome Installation](#42-chrome-installation)
   - [Firefox Installation](#43-firefox-installation)
   - [Edge Installation](#44-edge-installation)
   - [Brave Installation](#45-brave-installation)
   - [Verification](#46-verification)

5. [Core Concepts](#5-core-concepts)
   - [API Interception](#51-api-interception)
   - [Sensitive Data Detection](#52-sensitive-data-detection)
   - [Behavioral Baselines](#53-behavioral-baselines)
   - [Anomaly Detection](#54-anomaly-detection)
   - [Security Analysis](#55-security-analysis)

6. [Using the Tool](#6-using-the-tool)
   - [Dashboard Overview](#61-dashboard-overview)
   - [Requests Tab](#62-requests-tab)
   - [Findings Tab](#63-findings-tab)
   - [Domains Tab](#64-domains-tab)
   - [GraphQL Tab](#65-graphql-tab)
   - [Baselines Tab](#66-baselines-tab)
   - [Compare Tab](#67-compare-tab)
   - [Request Details](#68-request-details)

7. [Configuration](#7-configuration)
   - [General Settings](#71-general-settings)
   - [Ignored Domains](#72-ignored-domains)
   - [Custom Patterns](#73-custom-patterns)
   - [Notification Settings](#74-notification-settings)
   - [Export Settings](#75-export-settings)

8. [Detection Capabilities](#8-detection-capabilities)
   - [Sensitive Data Patterns](#81-sensitive-data-patterns)
   - [Security Header Analysis](#82-security-header-analysis)
   - [Cookie Security](#83-cookie-security)
   - [GraphQL Security](#84-graphql-security)
   - [Rate Limit Analysis](#85-rate-limit-analysis)
   - [Entropy-Based Detection](#86-entropy-based-detection)

9. [Export & Reporting](#9-export--reporting)
   - [JSON Export](#91-json-export)
   - [CSV Export](#92-csv-export)
   - [Markdown Reports](#93-markdown-reports)
   - [HTML Reports](#94-html-reports)
   - [SARIF Format](#95-sarif-format)

10. [Use Cases](#10-use-cases)
    - [VAPT Workflow](#101-vapt-workflow)
    - [SOC Monitoring](#102-soc-monitoring)
    - [Bug Bounty Hunting](#103-bug-bounty-hunting)
    - [Development Security](#104-development-security)

11. [Technical Implementation](#11-technical-implementation)
    - [Interception Techniques](#111-interception-techniques)
    - [Analysis Engine](#112-analysis-engine)
    - [Storage Strategy](#113-storage-strategy)
    - [Performance Optimization](#114-performance-optimization)

12. [Troubleshooting](#12-troubleshooting)
    - [Common Issues](#121-common-issues)
    - [Extension Not Working](#122-extension-not-working)
    - [Performance Issues](#123-performance-issues)
    - [Missing Requests](#124-missing-requests)

13. [Advanced Topics](#13-advanced-topics)
    - [Custom Detection Rules](#131-custom-detection-rules)
    - [Extending the Tool](#132-extending-the-tool)
    - [Integration with Other Tools](#133-integration-with-other-tools)

14. [Security & Privacy](#14-security--privacy)
    - [Data Handling](#141-data-handling)
    - [Permissions Explained](#142-permissions-explained)
    - [Best Practices](#143-best-practices)

15. [Appendix](#15-appendix)
    - [Complete Pattern Reference](#151-complete-pattern-reference)
    - [Keyboard Shortcuts](#152-keyboard-shortcuts)
    - [Glossary](#153-glossary)
    - [Changelog](#154-changelog)

---

# 1. Introduction

## 1.1 What is Shadow API Inspector?

Shadow API Inspector is a powerful browser extension designed to provide **real-time, comprehensive visibility** into client-side API interactions, third-party dependencies, and data flow patterns that traditional security tools miss.

Unlike proxy-based tools like Burp Suite or OWASP ZAP, Shadow API Inspector operates directly in the browser, intercepting API calls at the JavaScript level before they leave the browser. This gives it unique capabilities:

- **See what the browser sees**: Including authenticated sessions, CORS behavior, and actual headers
- **Zero configuration**: No proxy setup, certificate installation, or network changes required
- **Passive monitoring**: Works during normal browsing without interrupting your workflow
- **Real-time analysis**: Instant detection of sensitive data, security issues, and anomalies

## 1.2 Why Was It Built?

### The Modern Web Security Challenge

Modern web applications are fundamentally different from applications of 10 years ago:

| Then | Now |
|------|-----|
| Server-rendered pages | Single Page Applications (SPAs) |
| Few external dependencies | 50-200+ third-party API calls |
| Monolithic architecture | Microservices with dozens of APIs |
| Simple AJAX calls | GraphQL, WebSockets, Server-Sent Events |
| First-party code only | Heavy reliance on third-party JavaScript |

This evolution has created **massive blind spots** in traditional security testing:

1. **Proxy tools only capture what you explicitly test** - they miss the constant background API chatter of modern SPAs
2. **Third-party scripts can make API calls that bypass inspection** - analytics, ads, tracking pixels
3. **Client-side data exposure goes unnoticed** - APIs often return more data than the UI displays
4. **Supply chain attacks are nearly invisible** - how do you know if a third-party script suddenly starts calling new endpoints?

Shadow API Inspector was built to solve these problems by providing **continuous, passive monitoring** of all client-side API activity.

## 1.3 Who Is It For?

### Primary Audiences

| Audience | Primary Use Case |
|----------|-----------------|
| **VAPT Professionals** | Complete API surface discovery, vulnerability assessment, evidence collection |
| **SOC Analysts** | Real-time monitoring, anomaly detection, incident response |
| **Bug Bounty Hunters** | Finding hidden endpoints, data leakage, authentication issues |
| **Security Researchers** | Analyzing third-party behavior, supply chain security |
| **Developers** | Security testing during development, identifying data exposure |

### Key Benefits by Role

**For VAPT Teams:**
- Discover 100% of API endpoints in minutes, not days
- Automatically detect sensitive data in transit
- Generate evidence-ready reports
- Find shadow APIs and undocumented endpoints

**For SOC Teams:**
- Establish behavioral baselines for third-party services
- Real-time alerts for anomalous activity
- Detect supply chain compromises
- Monitor data exfiltration patterns

**For Bug Bounty Hunters:**
- Find hidden admin/debug endpoints
- Detect authentication bypasses
- Identify data leakage vulnerabilities
- Discover rate limiting gaps

## 1.4 Key Features Overview

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **API Interception** | Hooks fetch(), XHR, WebSocket, Beacon, EventSource, and dynamic script loading |
| **Sensitive Data Detection** | 35+ patterns for PII, auth tokens, cloud keys, financial data |
| **Behavioral Baselines** | Learns "normal" API behavior to detect anomalies |
| **GraphQL Analysis** | Extracts queries, detects introspection, calculates complexity |
| **Cookie Security** | Analyzes Set-Cookie headers for security issues |
| **Rate Limit Detection** | Identifies rate limiting patterns and gaps |
| **Real-time Alerts** | Desktop notifications for critical findings |
| **Multiple Export Formats** | JSON, CSV, Markdown, HTML, SARIF |

### What Gets Intercepted

\`\`\`
┌─────────────────────────────────────┐
│  Shadow API Inspector               │
├─────────────────────────────────────┤
│  ✓ fetch() API                      │
│  ✓ XMLHttpRequest (XHR)             │
│  ✓ WebSocket connections            │
│  ✓ Beacon API (sendBeacon)          │
│  ✓ EventSource (Server-Sent Events) │
│  ✓ Dynamic script loading           │
└─────────────────────────────────────┘
\`\`\`

---

# 2. The Problem Space

## 2.1 Third-Party API Blindness

Modern web applications rely heavily on third-party services:

- **Analytics**: Google Analytics, Mixpanel, Amplitude
- **Advertising**: Google Ads, Facebook Pixel, various ad networks
- **Customer Support**: Intercom, Zendesk, Drift
- **Payment Processing**: Stripe, PayPal, Braintree
- **Authentication**: Auth0, Okta, social logins
- **CDNs**: Cloudflare, Akamai, Fastly
- **Error Tracking**: Sentry, Bugsnag, Rollbar

**The Problem:**
- Each of these services makes API calls from your browser
- Traditional proxy tools don't capture this background traffic during normal browsing
- You have no visibility into what data is being sent to these services
- If a third-party script is compromised, you won't know

**Shadow API Inspector Solution:**
- Captures ALL API calls, including third-party
- Categorizes endpoints as internal vs. third-party vs. CDN
- Tracks what data is sent to each service
- Alerts on new third-party endpoints

## 2.2 Client-Side Data Leakage

APIs often return more data than the UI displays:

\`\`\`json
// API Response
{
  "user": {
    "id": 12345,
    "email": "user@example.com",
    "name": "John Doe",
    "role": "admin",
    "ssn": "123-45-6789",        // Never displayed
    "salary": 150000,             // Never displayed
    "internal_notes": "VIP",      // Never displayed
    "password_hash": "bcrypt..."  // CRITICAL - Never should be here
  }
}

// What the UI shows
┌─────────────────┐
│ Welcome, John!  │
│ Admin Account   │
└─────────────────┘
\`\`\`

**The Problem:**
- Developers fetch entire objects for convenience
- Sensitive data is exposed in API responses but never rendered
- This data is visible to anyone inspecting network traffic
- Attackers can harvest this data without triggering any server-side alerts

**Shadow API Inspector Solution:**
- Scans ALL response bodies for sensitive data patterns
- Detects PII, auth tokens, financial data, and more
- Calculates "data exposure score" (returned vs displayed)
- Alerts immediately when sensitive data is detected

## 2.3 Supply Chain Attacks

Supply chain attacks target the third-party services and scripts your application depends on:

**Attack Scenario:**
1. Attacker compromises a popular JavaScript library
2. The compromised code is served to all websites using that library
3. The malicious code harvests user data, credentials, or payment info
4. Data is exfiltrated to attacker-controlled servers

**Famous Examples:**
- **event-stream (2018)**: Malicious code added to steal cryptocurrency
- **ua-parser-js (2021)**: Cryptocurrency mining malware injected
- **Magecart attacks**: Payment skimmers injected into e-commerce sites

**The Problem:**
- No baseline of "normal" third-party behavior exists
- Cannot detect when a script starts calling new endpoints
- Traditional security tools don't monitor client-side changes
- By the time it's detected, data has already been stolen

**Shadow API Inspector Solution:**
- Establishes behavioral baselines for all third-party services
- Tracks which endpoints each third-party script calls
- Alerts when scripts start calling NEW endpoints
- Monitors data exfiltration patterns

## 2.4 Shadow APIs

"Shadow APIs" are endpoints that exist but aren't officially documented:

**Types of Shadow APIs:**
- **Undocumented internal APIs**: Used by frontend but not in public docs
- **Admin/debug endpoints**: Left accessible in production
- **Legacy API versions**: Old versions still functional
- **Mobile-specific APIs**: Designed for mobile apps but accessible from web
- **Partner APIs**: Intended for specific integrations

**Why They're Dangerous:**
- No security review because they're "not official"
- Often have weaker authentication
- May expose internal data or functionality
- Forgotten and unmaintained = unpatched vulnerabilities

**Shadow API Inspector Solution:**
- Discovers ALL endpoints the application calls
- Compares against documented API specifications (if provided)
- Flags endpoints not matching expected patterns
- Identifies admin/debug endpoint patterns

## 2.5 Real-Time Context Loss

Traditional security testing has a fundamental limitation: **point-in-time analysis**.

**The Problem:**
- You capture traffic during a testing session
- Application behavior changes based on user state, time, A/B tests
- You miss the "living" behavior of the application
- No correlation between API behavior and user actions

**Modern SPAs are Dynamic:**
- Background data synchronization
- Real-time updates via WebSockets
- Lazy-loaded content
- Personalized API responses
- Feature flags changing behavior

**Shadow API Inspector Solution:**
- Continuous passive monitoring during all browsing
- Captures API calls in context of user actions
- Tracks behavior over time (temporal analysis)
- Works with authenticated sessions naturally

---

# 3. Architecture Deep Dive

## 3.1 High-Level Overview

\`\`\`
┌─────────────────────────────────────────────────────────────────┐
│                         Browser                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                      Web Page                               │ │
│  │  ┌──────────────────────────────────────────────────────┐  │ │
│  │  │              Interceptor (injected)                   │  │ │
│  │  │  • Hooks fetch(), XHR, WebSocket, Beacon, SSE        │  │ │
│  │  │  • Captures request/response data                     │  │ │
│  │  │  • Dispatches to Content Script                       │  │ │
│  │  └───────────────────────┬──────────────────────────────┘  │ │
│  └──────────────────────────┼─────────────────────────────────┘ │
│                             │ CustomEvent                        │
│  ┌──────────────────────────▼─────────────────────────────────┐ │
│  │                   Content Script                            │ │
│  │  • Receives intercepted data                                │ │
│  │  • Forwards to Background Service Worker                    │ │
│  └──────────────────────────┬─────────────────────────────────┘ │
│                             │ chrome.runtime.sendMessage         │
│  ┌──────────────────────────▼─────────────────────────────────┐ │
│  │              Background Service Worker                      │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │ │
│  │  │  Analysis   │  │  Baseline   │  │    Notification     │ │ │
│  │  │   Engine    │  │   Manager   │  │      Manager        │ │ │
│  │  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │ │
│  │         │                │                     │            │ │
│  │  ┌──────▼────────────────▼─────────────────────▼──────────┐ │ │
│  │  │                Storage Manager (IndexedDB)             │ │ │
│  │  │  • Requests  • Settings  • Baselines  • Custom Rules   │ │ │
│  │  └────────────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌────────────────────┐  ┌────────────────────────────────────┐ │
│  │   Popup Dashboard  │  │          Options Page              │ │
│  │  • View requests   │  │  • Configure settings              │ │
│  │  • See findings    │  │  • Manage ignored domains          │ │
│  │  • Export data     │  │  • Add custom patterns             │ │
│  └────────────────────┘  └────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
\`\`\`

## 3.2 File Structure

\`\`\`
shadow-api-inspector/
│
├── manifest.json              # Chrome/Edge/Brave manifest (V3)
├── manifest.firefox.json      # Firefox manifest (V2)
│
├── background/
│   ├── service-worker.js      # Main background script
│   ├── analysis-engine.js     # Sensitive data & security analysis
│   ├── storage-manager.js     # IndexedDB operations
│   ├── baseline-manager.js    # Behavioral baseline & anomaly detection
│   ├── graphql-analyzer.js    # GraphQL-specific analysis
│   ├── rate-limit-detector.js # Rate limit detection
│   ├── notification-manager.js# Desktop notifications
│   ├── export-manager.js      # Multi-format export
│   └── polyfills.js           # Cross-browser compatibility
│
├── content/
│   ├── injector.js            # Injects interceptor into page
│   └── interceptor.js         # API hooks (runs in page context)
│
├── popup/
│   ├── popup.html             # Dashboard UI
│   ├── popup.css              # Dashboard styles
│   └── popup.js               # Dashboard logic
│
├── options/
│   ├── options.html           # Settings page UI
│   ├── options.css            # Settings styles
│   └── options.js             # Settings logic
│
├── icons/
│   ├── icon-16.png
│   ├── icon-32.png
│   ├── icon-48.png
│   └── icon-128.png
│
└── docs/
    └── SHADOW-API-INSPECTOR-DOCUMENTATION.md  # This file
\`\`\`

## 3.3 Component Breakdown

### 3.3.1 Interceptor (`content/interceptor.js`)

The interceptor runs in the **page context** (not the isolated content script world). This is critical because it needs access to the page's actual JavaScript objects.

**What it hooks:**

| API | Method | Purpose |
|-----|--------|---------|
| `window.fetch` | Override | Modern HTTP requests |
| `XMLHttpRequest.prototype.open` | Override | Legacy HTTP requests |
| `XMLHttpRequest.prototype.send` | Override | Capture request body |
| `XMLHttpRequest.prototype.setRequestHeader` | Override | Capture headers |
| `window.WebSocket` | Replace constructor | Real-time connections |
| `navigator.sendBeacon` | Override | Analytics/tracking |
| `window.EventSource` | Replace constructor | Server-Sent Events |
| `document.createElement` | Override | Dynamic script detection |

**How it works:**

\`\`\`javascript
// Example: Fetch interception
const originalFetch = window.fetch;
window.fetch = async function(...args) {
  // Capture request details
  const requestData = captureRequest(args);
  
  try {
    // Call original fetch
    const response = await originalFetch.apply(this, args);
    
    // Capture response details
    captureResponse(response.clone(), requestData);
    
    // Return original response (transparent to application)
    return response;
  } catch (error) {
    captureError(error, requestData);
    throw error;
  }
};
\`\`\`

### 3.3.2 Analysis Engine (`background/analysis-engine.js`)

The analysis engine is the core intelligence of the extension. It processes every captured request/response.

**Capabilities:**

1. **Sensitive Data Detection**
   - 35+ regex patterns for different data types
   - Validation functions to reduce false positives
   - Luhn algorithm for credit card validation
   - Entropy calculation for potential secrets

2. **Security Header Analysis**
   - Checks for missing security headers
   - CORS policy analysis
   - Cookie security flags

3. **Endpoint Classification**
   - Internal vs. third-party vs. CDN
   - API versioning detection
   - GraphQL endpoint identification

### 3.3.3 Baseline Manager (`background/baseline-manager.js`)

The baseline manager implements behavioral analysis.

**Learning Phase:**
- First 100 requests per domain = learning period
- Tracks: endpoints, response sizes, data types, auth methods, status codes

**Detection Phase:**
- Compares new requests against established baseline
- Flags: new endpoints, size anomalies, new data types, new auth methods

### 3.3.4 Storage Manager (`background/storage-manager.js`)

Uses IndexedDB for persistent storage.

**Stores:**

| Store | Purpose | Retention |
|-------|---------|-----------|
| `requests` | Captured request/response data | Configurable (default 7 days) |
| `settings` | User preferences | Permanent |
| `baselines` | Behavioral baselines | Permanent (until reset) |
| `customRules` | User-defined patterns | Permanent |

## 3.4 Data Flow

\`\`\`
User browses website
         │
         ▼
    ┌─────────┐
    │  fetch  │ ← Application makes API call
    └────┬────┘
         │
         ▼
┌─────────────────┐
│   Interceptor   │ ← Hooks intercept the call
│  (page context) │
└────────┬────────┘
         │ CustomEvent('__shadowApi_request')
         ▼
┌─────────────────┐
│ Content Script  │ ← Receives in isolated world
│   (injector)    │
└────────┬────────┘
         │ chrome.runtime.sendMessage
         ▼
┌─────────────────┐
│ Service Worker  │ ← Background processing
│                 │
│  ┌───────────┐  │
│  │ Analysis  │  │ ← Sensitive data detection
│  │  Engine   │  │
│  └─────┬─────┘  │
│        │        │
│  ┌─────▼─────┐  │
│  │ Baseline  │  │ ← Anomaly detection
│  │  Manager  │  │
│  └─────┬─────┘  │
│        │        │
│  ┌─────▼─────┐  │
│  │ Storage   │  │ ← Persist to IndexedDB
│  │  Manager  │  │
│  └─────┬─────┘  │
│        │        │
│  ┌─────▼─────┐  │
│  │  Notify   │  │ ← Alert if critical
│  │  Manager  │  │
│  └───────────┘  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Popup/Options  │ ← User views results
└─────────────────┘
\`\`\`

## 3.5 Cross-Browser Compatibility

The extension supports multiple browsers with different manifest versions:

| Browser | Manifest Version | Background Script |
|---------|-----------------|-------------------|
| Chrome 88+ | V3 | Service Worker |
| Edge 88+ | V3 | Service Worker |
| Brave | V3 | Service Worker |
| Firefox | V2 | Background Script |

**Key Differences:**

| Feature | Manifest V3 | Manifest V2 (Firefox) |
|---------|-------------|----------------------|
| Background | `service_worker` | `scripts` array |
| Action | `action` | `browser_action` |
| Host Permissions | Separate key | In `permissions` |
| API Namespace | `chrome.*` | `browser.*` |

The `polyfills.js` file handles API namespace differences:

\`\`\`javascript
// Normalize browser API
if (typeof browser !== 'undefined') {
  // Firefox - browser.* APIs
  globalThis.chrome = browser;
}
\`\`\`

---

# 4. Installation Guide

## 4.1 Requirements

### Minimum Browser Versions

| Browser | Minimum Version | Manifest |
|---------|----------------|----------|
| Google Chrome | 88+ | V3 |
| Microsoft Edge | 88+ | V3 |
| Brave | Latest | V3 |
| Mozilla Firefox | 109+ | V2 |

### System Requirements

- Any operating system (Windows, macOS, Linux)
- ~50MB available memory
- ~10MB storage for extension + data

## 4.2 Chrome Installation

### Method 1: Developer Mode (Recommended for Development)

1. **Download/Clone the Extension**
   \`\`\`bash
   git clone https://github.com/your-repo/shadow-api-inspector.git
   # Or download and extract ZIP
   \`\`\`

2. **Open Chrome Extensions**
   - Navigate to `chrome://extensions/`
   - Or: Menu → More Tools → Extensions

3. **Enable Developer Mode**
   - Toggle "Developer mode" switch in top-right corner

4. **Load the Extension**
   - Click "Load unpacked"
   - Select the `shadow-api-inspector` folder (containing `manifest.json`)

5. **Pin the Extension**
   - Click the puzzle piece icon in toolbar
   - Pin "Shadow API Inspector"

### Method 2: Chrome Web Store (When Published)

1. Visit the Chrome Web Store listing
2. Click "Add to Chrome"
3. Confirm the permissions

## 4.3 Firefox Installation

### Step 1: Use Firefox Manifest

Rename or copy the Firefox-specific manifest:

\`\`\`bash
# Backup original
mv manifest.json manifest.chrome.json

# Use Firefox manifest
cp manifest.firefox.json manifest.json
\`\`\`

### Step 2: Load as Temporary Add-on

1. Open Firefox
2. Navigate to `about:debugging#/runtime/this-firefox`
3. Click "Load Temporary Add-on..."
4. Select `manifest.json` from the extension folder

**Note:** Temporary add-ons are removed when Firefox closes. For permanent installation, you need to:
- Submit to Firefox Add-ons (AMO), or
- Use `web-ext` tool for development

### Step 3: Using web-ext (Recommended for Development)

\`\`\`bash
# Install web-ext
npm install -g web-ext

# Run extension
cd shadow-api-inspector
web-ext run

# This opens Firefox with the extension loaded
\`\`\`

## 4.4 Edge Installation

Edge uses the same Manifest V3 as Chrome:

1. **Open Edge Extensions**
   - Navigate to `edge://extensions/`

2. **Enable Developer Mode**
   - Toggle "Developer mode" switch

3. **Load Extension**
   - Click "Load unpacked"
   - Select the extension folder

4. **Pin to Toolbar**
   - Click the extensions menu
   - Pin Shadow API Inspector

## 4.5 Brave Installation

Brave is Chromium-based and supports Chrome extensions:

1. **Open Brave Extensions**
   - Navigate to `brave://extensions/`

2. **Enable Developer Mode**
   - Toggle the switch

3. **Load Extension**
   - Click "Load unpacked"
   - Select the extension folder

## 4.6 Verification

After installation, verify the extension is working:

### Quick Test

1. Open the extension popup (click the icon)
2. Navigate to any website (e.g., `https://jsonplaceholder.typicode.com/posts`)
3. The popup should show captured API requests
4. Check that the request count increases

### Console Verification

1. Open browser DevTools (F12)
2. Look for: `[Shadow API Inspector] Interception active`
3. This confirms the interceptor is loaded

### Test Sensitive Data Detection

1. Visit: `https://jsonplaceholder.typicode.com/users`
2. Open the extension popup
3. You should see email addresses detected in findings

---

# 5. Core Concepts

## 5.1 API Interception

### How It Works

Shadow API Inspector uses **JavaScript API hooking** to intercept network requests. This is fundamentally different from proxy-based tools:

| Proxy-Based (Burp/ZAP) | Browser-Based (Shadow API) |
|-----------------------|---------------------------|
| Intercepts at network level | Intercepts at JavaScript level |
| Requires proxy configuration | Zero configuration |
| Requires certificate installation | No certificates needed |
| Can modify traffic | Read-only (by design) |
| Misses some client-side calls | Catches everything |
| External to browser | Inside the browser |

### Interception Points

**1. fetch() API**
\`\`\`javascript
// Modern HTTP requests
fetch('/api/users')
  .then(response => response.json())
  .then(data => console.log(data));
\`\`\`

**2. XMLHttpRequest**
\`\`\`javascript
// Legacy HTTP requests
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/data');
xhr.send();
\`\`\`

**3. WebSocket**
\`\`\`javascript
// Real-time connections
const ws = new WebSocket('wss://api.example.com/socket');
ws.send(JSON.stringify({ action: 'subscribe' }));
\`\`\`

**4. Beacon API**
\`\`\`javascript
// Analytics & tracking (fire-and-forget)
navigator.sendBeacon('/analytics', data);
\`\`\`

**5. EventSource (Server-Sent Events)**
\`\`\`javascript
// Server push
const es = new EventSource('/events');
es.onmessage = (e) => console.log(e.data);
\`\`\`

**6. Dynamic Script Loading**
\`\`\`javascript
// Third-party script injection
const script = document.createElement('script');
script.src = 'https://analytics.example.com/tracker.js';
document.body.appendChild(script);
\`\`\`

### What Gets Captured

For each request, the extension captures:

| Field | Description |
|-------|-------------|
| `id` | Unique request identifier |
| `type` | Request type (fetch, xhr, websocket, beacon, sse, script) |
| `url` | Full request URL |
| `method` | HTTP method (GET, POST, etc.) |
| `requestHeaders` | All request headers |
| `requestBody` | Request payload (if any) |
| `status` | HTTP status code |
| `statusText` | Status message |
| `responseHeaders` | All response headers |
| `responseBody` | Response payload |
| `duration` | Request duration in ms |
| `timestamp` | When the request was made |

## 5.2 Sensitive Data Detection

### Detection Approach

The extension uses a **multi-layer detection strategy**:

\`\`\`
Layer 1: Regex Patterns
         │
         ▼ (matches)
Layer 2: Validation Functions
         │
         ▼ (validated)
Layer 3: Entropy Analysis
         │
         ▼ (high entropy)
Finding Reported
\`\`\`

### Pattern Categories

**1. Personal Identifiable Information (PII)**
- Email addresses
- Phone numbers
- Social Security Numbers
- Passport numbers

**2. Authentication Credentials**
- JWT tokens
- API keys (generic)
- Bearer tokens
- Basic auth credentials
- Session tokens

**3. Cloud Provider Secrets**
- AWS Access Keys (`AKIA...`)
- AWS Secret Keys
- Google API keys (`AIza...`)
- Google OAuth tokens (`ya29...`)
- Azure Storage connection strings
- Firebase URLs

**4. Version Control & CI/CD**
- GitHub tokens (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`)
- GitLab tokens (`glpat-...`)
- NPM tokens (`npm_...`)
- PyPI tokens

**5. Communication Services**
- Slack tokens (`xoxb-`, `xoxp-`, etc.)
- Slack webhooks
- Discord webhooks
- Twilio SID/Auth tokens
- SendGrid keys

**6. Payment & Financial**
- Credit card numbers (with Luhn validation)
- Stripe keys (`sk_live_`, `sk_test_`, `pk_...`)
- IBAN
- Bitcoin addresses
- Ethereum addresses

**7. Technical Exposure**
- Internal IP addresses
- Database connection strings
- Stack traces
- Private keys

### Severity Levels

| Level | Meaning | Examples |
|-------|---------|----------|
| **Critical** | Immediate security risk | AWS keys, private keys, database credentials |
| **High** | Significant issue | JWT tokens, API keys, credit cards |
| **Medium** | Moderate concern | Email addresses, internal IPs |
| **Low** | Informational | Public API keys, debug messages |

## 5.3 Behavioral Baselines

### Concept

A **behavioral baseline** represents "normal" API behavior for a domain. Once established, any deviation triggers an anomaly alert.

### Learning Phase

When you first visit a domain, the extension enters a **learning phase**:

\`\`\`
First 100 requests to example.com
         │
         ▼
┌─────────────────────────┐
│    Learning Phase       │
│                         │
│  Tracking:              │
│  • Endpoints called     │
│  • Response sizes       │
│  • Data types returned  │
│  • Auth methods used    │
│  • Status codes seen    │
│  • Request frequency    │
└────────────┬────────────┘
             │
             ▼ (after 100 requests)
┌─────────────────────────┐
│   Baseline Established  │
│                         │
│  Now monitoring for:    │
│  • New endpoints        │
│  • Size anomalies       │
│  • New data types       │
│  • Auth changes         │
│  • Unusual statuses     │
└─────────────────────────┘
\`\`\`

### What Gets Baselined

| Metric | How It's Used |
|--------|--------------|
| **Endpoints** | List of all paths called (normalized) |
| **Response Sizes** | Average and standard deviation |
| **Data Types** | Types of sensitive data seen |
| **Auth Methods** | Bearer, Basic, API Key, Cookie, etc. |
| **Status Codes** | Distribution of HTTP statuses |
| **Headers** | Common request headers |

### Path Normalization

To properly baseline endpoints, paths are normalized:

\`\`\`
/users/12345/posts  →  /users/{id}/posts
/items/abc-123-def →  /items/{uuid}
/v2/api/data       →  /v2/api/data
\`\`\`

This ensures that `/users/1/posts` and `/users/999/posts` are recognized as the same endpoint.

## 5.4 Anomaly Detection

### Types of Anomalies

**1. New Endpoint**
\`\`\`
Baseline: [GET /api/users, POST /api/login]
New Request: GET /api/admin/config
→ ANOMALY: New endpoint detected
\`\`\`

**2. Response Size Anomaly**
\`\`\`
Baseline: avg=2KB, stddev=0.5KB
New Response: 50KB
→ ANOMALY: Response 96 standard deviations from mean
\`\`\`

**3. New Data Type**
\`\`\`
Baseline: [email, name]
New Response contains: credit_card
→ ANOMALY: New sensitive data type detected
\`\`\`

**4. New Authentication Method**
\`\`\`
Baseline: [Bearer token]
New Request uses: Basic auth
→ ANOMALY: New authentication method detected
\`\`\`

**5. Unusual Status Code**
\`\`\`
Baseline: [200, 201, 400, 404]
New Response: 500
→ ANOMALY: New status code detected
\`\`\`

### Anomaly Severity

| Anomaly Type | Default Severity |
|--------------|-----------------|
| New Endpoint | Medium |
| Response Size (>4 stddev) | High |
| Response Size (2-4 stddev) | Medium |
| New Data Type | High |
| New Auth Method | Medium |
| New Status Code (error) | Medium |
| New Status Code (success) | Low |

## 5.5 Security Analysis

### Security Header Checks

The extension checks for missing security headers:

| Header | Purpose | Finding if Missing |
|--------|---------|-------------------|
| `Strict-Transport-Security` | Force HTTPS | Medium |
| `X-Content-Type-Options` | Prevent MIME sniffing | Medium |
| `X-Frame-Options` | Prevent clickjacking | Medium |
| `Content-Security-Policy` | XSS protection | Medium |

### CORS Analysis

Detects potentially dangerous CORS configurations:

\`\`\`
Access-Control-Allow-Origin: *
→ FINDING: Wildcard CORS policy detected (Medium)

Access-Control-Allow-Credentials: true
+ Access-Control-Allow-Origin: *
→ FINDING: Dangerous CORS configuration (High)
\`\`\`

### Cookie Security Analysis

Checks Set-Cookie headers for security issues:

| Issue | Severity | Description |
|-------|----------|-------------|
| Missing `Secure` flag on HTTPS | High | Cookie can be sent over HTTP |
| Missing `HttpOnly` on sensitive cookie | High | Cookie accessible to JavaScript |
| Missing `SameSite` attribute | Medium | CSRF vulnerability |
| `SameSite=None` without `Secure` | High | Invalid configuration |
| Overly broad domain | Medium | Cookie sent to all subdomains |
| Long expiration on sensitive cookie | Low | Extended attack window |

---

# 6. Using the Tool

## 6.1 Dashboard Overview

The popup dashboard is your primary interface. Access it by clicking the extension icon.

\`\`\`
┌─────────────────────────────────────────────┐
│  Shadow API Inspector                    ≡  │
├─────────────────────────────────────────────┤
│  [Requests] [Findings] [Domains] [GraphQL]  │
│  [Baselines] [Compare]                      │
├─────────────────────────────────────────────┤
│                                             │
│         ┌─────────────────────┐             │
│         │    Main Content     │             │
│         │    (Tab-specific)   │             │
│         │                     │             │
│         └─────────────────────┘             │
│                                             │
├─────────────────────────────────────────────┤
│  [Clear] [Export ▼] [⚙ Settings]           │
└─────────────────────────────────────────────┘
\`\`\`

### Header Controls

| Element | Function |
|---------|----------|
| Title | "Shadow API Inspector" |
| Menu (≡) | Additional options |
| Tabs | Switch between views |

### Footer Controls

| Button | Function |
|--------|----------|
| Clear | Delete all captured data |
| Export | Download data (JSON, CSV, Markdown, HTML, SARIF) |
| Settings | Open options page |

## 6.2 Requests Tab

The Requests tab shows all captured API calls in chronological order (newest first).

### Request List

\`\`\`
┌─────────────────────────────────────────────┐
│ ● POST /api/login              200   145ms │
│   api.example.com              2.3 KB      │
├─────────────────────────────────────────────┤
│ ○ GET /api/users               200   89ms  │
│   api.example.com              15.2 KB     │
├─────────────────────────────────────────────┤
│ ○ GET /analytics/track         204   23ms  │
│   analytics.google.com         0 B         │
└─────────────────────────────────────────────┘
\`\`\`

### Visual Indicators

| Indicator | Meaning |
|-----------|---------|
| 🔴 Red dot | Critical finding |
| 🟠 Orange dot | High severity finding |
| 🟡 Yellow dot | Medium severity finding |
| 🟢 Green dot | Low/no findings |
| ⚪ Gray dot | Info only |

### Filters

| Filter | Options |
|--------|---------|
| Method | All, GET, POST, PUT, DELETE, PATCH, WS, SSE |
| Status | All, 2xx, 3xx, 4xx, 5xx, Error |
| Type | All, Fetch, XHR, WebSocket, Beacon, SSE, Script |
| Domain | Dropdown of captured domains |
| Search | Free-text search in URLs |

### Request Actions

Click any request to see details. Right-click for:
- Copy URL
- Copy as cURL
- Replay request
- Add to comparison

## 6.3 Findings Tab

The Findings tab aggregates all security findings across all requests.

### Finding Card

\`\`\`
┌─────────────────────────────────────────────┐
│ 🔴 CRITICAL                                 │
│ AWS Access Key detected                      │
├─────────────────────────────────────────────┤
│ URL: /api/config                            │
│ Location: responseBody                       │
│ Pattern: AKIA****************               │
├─────────────────────────────────────────────┤
│ [View Request]                              │
└─────────────────────────────────────────────┘
\`\`\`

### Filtering Findings

| Filter | Options |
|--------|---------|
| Severity | Critical, High, Medium, Low, All |
| Type | PII, Authentication, Cloud, Financial, Security, Cookie |
| Domain | Specific domain or all |

### Finding Types

| Type | Examples |
|------|----------|
| **PII** | Email, phone, SSN, passport |
| **Authentication** | JWT, API keys, tokens |
| **Cloud** | AWS keys, GCP keys, Azure secrets |
| **Financial** | Credit cards, bank accounts |
| **Security Headers** | Missing HSTS, CSP, etc. |
| **Cookie** | Insecure cookie settings |
| **CORS** | Wildcard origins, credential exposure |

## 6.4 Domains Tab

The Domains tab shows all unique domains contacted, categorized by type.

### Domain Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Internal** | Same origin as page | api.yoursite.com |
| **Third-Party** | Different origin | api.stripe.com, auth0.com |
| **CDN** | Content delivery networks | cloudflare.com, akamaihd.net |

### Domain Card

\`\`\`
┌─────────────────────────────────────────────┐
│ 📊 api.example.com                [Internal]│
├─────────────────────────────────────────────┤
│ Requests: 47                                │
│ Endpoints: 12                               │
│ Methods: GET, POST, PUT                     │
│ Findings: 3 (1 critical)                    │
├─────────────────────────────────────────────┤
│ [View Requests] [View Baseline]             │
└─────────────────────────────────────────────┘
\`\`\`

## 6.5 GraphQL Tab

The GraphQL tab provides specialized analysis for GraphQL APIs.

### Overview

\`\`\`
┌─────────────────────────────────────────────┐
│ GraphQL Endpoints                           │
├─────────────────────────────────────────────┤
│ • https://api.example.com/graphql           │
│   Introspection: ✓ Enabled (Warning)        │
├─────────────────────────────────────────────┤
│ Queries: 15  Mutations: 8  Subscriptions: 0│
└─────────────────────────────────────────────┘
\`\`\`

### Query Analysis

For each GraphQL operation:

| Field | Description |
|-------|-------------|
| Operation Type | query, mutation, subscription |
| Operation Name | Named operation or "anonymous" |
| Depth | Nesting level of query |
| Complexity | Calculated complexity score |
| Fields | Top-level fields requested |
| Findings | Security issues detected |

### GraphQL Security Findings

| Finding | Severity | Description |
|---------|----------|-------------|
| Introspection Enabled | Medium | Schema exposed to attackers |
| Deep Query | High | Depth >10, potential DoS |
| High Complexity | Medium | Complexity >100, resource exhaustion |
| Unauthenticated Mutation | High | Mutation without auth headers |
| Sensitive Field Access | Medium | Accessing password, token, etc. |

## 6.6 Baselines Tab

The Baselines tab shows behavioral baselines and anomalies.

### Baseline Status

\`\`\`
┌─────────────────────────────────────────────┐
│ api.example.com                             │
├─────────────────────────────────────────────┤
│ Status: ✓ Active                            │
│ Established: 2024-01-15                     │
│ Endpoints: 23                               │
│ Data Types: email, name, id                 │
│ Auth Methods: Bearer                        │
├─────────────────────────────────────────────┤
│ Recent Anomalies:                           │
│ • New endpoint: /api/admin/users (Medium)   │
│ • Response size spike: 50KB (High)          │
├─────────────────────────────────────────────┤
│ [View Details] [Reset Baseline]             │
└─────────────────────────────────────────────┘
\`\`\`

### Baseline Phases

| Phase | Icon | Description |
|-------|------|-------------|
| Learning | 📚 | Collecting initial data (0-100 requests) |
| Active | ✓ | Baseline established, monitoring for anomalies |
| Stale | ⚠ | No requests in 7+ days |

## 6.7 Compare Tab

The Compare tab allows side-by-side comparison of two requests.

### How to Use

1. In Requests tab, select first request (click checkbox)
2. Select second request
3. Click "Compare Selected" or switch to Compare tab

### Comparison View

\`\`\`
┌───────────────────┬───────────────────┐
│ Request A         │ Request B         │
├───────────────────┼───────────────────┤
│ POST /api/login   │ POST /api/login   │
│ Status: 200       │ Status: 401       │
├───────────────────┼───────────────────┤
│ Headers:          │ Headers:          │
│ Auth: Bearer xyz  │ Auth: Bearer abc  │ ← Different
│ Content-Type: ... │ Content-Type: ... │
├───────────────────┼───────────────────┤
│ Body:             │ Body:             │
│ {"user":"admin"}  │ {"user":"admin"}  │
└───────────────────┴───────────────────┘
\`\`\`

### Use Cases

- Compare successful vs. failed auth attempts
- Identify parameter differences
- Analyze response variations
- Debug intermittent issues

## 6.8 Request Details

Clicking any request opens the detail view.

### Detail Tabs

**Headers Tab**
\`\`\`
Request Headers:
┌─────────────────────────────────────────────┐
│ Authorization: Bearer eyJhbGc...            │ ← Highlighted
│ Content-Type: application/json              │
│ Accept: */*                                 │
│ User-Agent: Mozilla/5.0...                  │
└─────────────────────────────────────────────┘

Response Headers:
┌─────────────────────────────────────────────┐
│ Content-Type: application/json              │
│ X-RateLimit-Remaining: 99                   │
│ Set-Cookie: session=abc; HttpOnly           │
└─────────────────────────────────────────────┘
\`\`\`

**Body Tab**
\`\`\`json
{
  "user": {
    "id": 12345,
    "email": "user@example.com",  // ← Highlighted (PII)
    "name": "John Doe"
  }
}
\`\`\`

**Cookies Tab**
\`\`\`
┌─────────────────────────────────────────────┐
│ session                                     │
│ Value: abc123...                            │
│ Secure: ✓  HttpOnly: ✓  SameSite: Strict   │
│ Status: ✓ Secure                            │
├─────────────────────────────────────────────┤
│ tracking                                    │
│ Value: xyz789...                            │
│ Secure: ✗  HttpOnly: ✗  SameSite: None     │
│ Status: ⚠ 3 Issues                         │
└─────────────────────────────────────────────┘
\`\`\`

**Timing Tab**
\`\`\`
DNS Lookup:     12ms  ████
TCP Connect:    23ms  ████████
TLS Handshake:  45ms  ████████████████
Request:         8ms  ███
Response:       67ms  ████████████████████████
Total:         155ms
\`\`\`

**Findings Tab**
\`\`\`
┌─────────────────────────────────────────────┐
│ 🟡 MEDIUM: Email address detected           │
│ Location: responseBody.user.email           │
│ Value: u***@example.com                     │
├─────────────────────────────────────────────┤
│ 🟢 LOW: Internal IP detected                │
│ Location: responseBody.debug.server_ip      │
│ Value: 10.0.***.***                         │
└─────────────────────────────────────────────┘
\`\`\`

### Actions

| Action | Description |
|--------|-------------|
| Copy URL | Copy full URL to clipboard |
| Copy as cURL | Copy as cURL command |
| Replay | Re-send the request |
| Compare | Add to comparison |
| Export | Export this request only |

---

# 7. Configuration

## 7.1 General Settings

Access settings via the gear icon or `Options` in extension menu.

### Capture Settings

| Setting | Description | Default |
|---------|-------------|---------|
| Enable Capture | Master on/off switch | On |
| Capture Fetch | Intercept fetch() calls | On |
| Capture XHR | Intercept XMLHttpRequest | On |
| Capture WebSocket | Intercept WebSocket | On |
| Capture Beacon | Intercept sendBeacon | On |
| Capture SSE | Intercept EventSource | On |
| Capture Scripts | Detect dynamic scripts | On |

### Data Retention

| Setting | Description | Default |
|---------|-------------|---------|
| Retention Days | How long to keep data | 7 days |
| Max Requests | Maximum requests stored | 10,000 |
| Auto Cleanup | Automatically remove old data | On |

## 7.2 Ignored Domains

Domains in this list will not be captured or analyzed.

### Default Ignored Domains

\`\`\`
localhost
127.0.0.1
*.local
\`\`\`

### Adding Ignored Domains

\`\`\`
# Exact match
google-analytics.com

# Wildcard subdomain
*.google.com

# All subdomains and domain
**.facebook.com
\`\`\`

### When to Ignore

- Trusted first-party analytics
- Known benign third-party services
- Development/testing domains
- High-frequency low-value endpoints

## 7.3 Custom Patterns

Add your own sensitive data detection patterns.

### Pattern Format

\`\`\`yaml
name: "Custom API Key"
pattern: "MYAPP_[A-Za-z0-9]{32}"
type: "Authentication"
severity: "critical"
description: "MyApp API key detected"
\`\`\`

### Pattern Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier |
| `pattern` | Yes | Regular expression |
| `type` | Yes | Category (PII, Authentication, etc.) |
| `severity` | Yes | critical, high, medium, low |
| `description` | Yes | Human-readable description |
| `validate` | No | Additional validation function |

### Example Custom Patterns

**Internal Employee ID:**
\`\`\`yaml
name: "Employee ID"
pattern: "EMP-[0-9]{6}"
type: "PII"
severity: "medium"
description: "Internal employee ID detected"
\`\`\`

**Custom Token Format:**
\`\`\`yaml
name: "Internal Auth Token"
pattern: "IAT_[a-f0-9]{64}"
type: "Authentication"
severity: "critical"
description: "Internal authentication token detected"
\`\`\`

## 7.4 Notification Settings

Configure desktop notifications for security findings.

### Severity Thresholds

| Severity | Notify | Sound | Require Interaction |
|----------|--------|-------|---------------------|
| Critical | Yes | Yes | Yes |
| High | Yes | No | No |
| Medium | No | No | No |
| Low | No | No | No |

### Notification Options

| Setting | Description | Default |
|---------|-------------|---------|
| Enable Notifications | Master switch | On |
| Rate Limit | Max notifications per minute | 5 |
| Batch Notifications | Group multiple findings | On |
| Sound | Play sound for critical | On |

## 7.5 Export Settings

Configure default export behavior.

| Setting | Description | Default |
|---------|-------------|---------|
| Default Format | Preferred export format | JSON |
| Include Request Bodies | Include full request payloads | Yes |
| Include Response Bodies | Include full response payloads | Yes |
| Mask Sensitive Data | Partially redact detected secrets | Yes |
| Pretty Print | Format JSON output | Yes |

---

# 8. Detection Capabilities

## 8.1 Sensitive Data Patterns

Complete list of built-in detection patterns:

### PII (Personally Identifiable Information)

| Pattern Name | Regex | Example Match |
|--------------|-------|---------------|
| Email | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | user@example.com |
| Phone (US) | `(\+?1?[-.\s]?)?$$?\d{3}$$?[-.\s]?\d{3}[-.\s]?\d{4}` | (555) 123-4567 |
| SSN | `\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b` | 123-45-6789 |
| Passport | `\b[A-Z]{1,2}[0-9]{6,9}\b` | AB1234567 |

### Authentication Tokens

| Pattern Name | Regex | Example Match |
|--------------|-------|---------------|
| JWT | `eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*` | eyJhbGc... |
| Bearer Token | `Bearer\s+[A-Za-z0-9_-]+` | Bearer abc123... |
| Basic Auth | `Basic\s+[A-Za-z0-9+/=]+` | Basic dXNlcjpwYXNz |
| API Key (generic) | `api[_-]?key.*[a-zA-Z0-9_-]{20,}` | api_key=abc123... |

### Cloud Provider Secrets

| Pattern Name | Regex | Example Match |
|--------------|-------|---------------|
| AWS Access Key | `AKIA[0-9A-Z]{16}` | AKIAIOSFODNN7EXAMPLE |
| AWS Secret Key | `aws.?secret.*[A-Za-z0-9/+=]{40}` | aws_secret_key=wJal... |
| Google API Key | `AIza[0-9A-Za-z_-]{35}` | AIzaSyC2sVn... |
| Google OAuth | `ya29\.[0-9A-Za-z_-]+` | ya29.a0AfH6... |
| Azure Storage | `DefaultEndpointsProtocol=https;AccountName=...` | Full connection string |
| Firebase URL | `https://[a-z0-9-]+\.firebaseio\.com` | https://myapp.firebaseio.com |

### Version Control & CI/CD

| Pattern Name | Regex | Example Match |
|--------------|-------|---------------|
| GitHub Token (new) | `gh[pousr]_[A-Za-z0-9_]{36,}` | ghp_xxxxxxxxxxxx |
| GitLab PAT | `glpat-[A-Za-z0-9_-]{20,}` | glpat-xxxxxxxxxx |
| NPM Token | `npm_[A-Za-z0-9]{36}` | npm_xxxxxxxxxxxx |
| PyPI Token | `pypi-AgEIcHlwaS5vcmc[A-Za-z0-9_-]{50,}` | pypi-AgEIcHlw... |

### Communication Services

| Pattern Name | Regex | Example Match |
|--------------|-------|---------------|
| Slack Token | `xox[baprs]-[0-9]{10,13}-[0-9]{10,13}[a-zA-Z0-9-]*` | xoxb-123456789-... |
| Slack Webhook | `https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]+` | https://hooks.slack.com/... |
| Discord Webhook | `https://discord(app)?\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+` | https://discord.com/api/... |
| Twilio SID | `AC[a-f0-9]{32}` | ACxxxxxxxxxxxxxxxx |
| Twilio Auth | `SK[a-f0-9]{32}` | SKxxxxxxxxxxxxxxxx |
| SendGrid | `SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}` | SG.xxxxxx.xxxxxx |

### Financial

| Pattern Name | Regex | Validation |
|--------------|-------|------------|
| Credit Card | `\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|...)\b` | Luhn algorithm |
| IBAN | `\b[A-Z]{2}[0-9]{2}[A-Z0-9]{4}[0-9]{7}(?:[A-Z0-9]?){0,16}\b` | Format check |
| Bitcoin | `\b(?:bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}\b` | Address format |
| Ethereum | `\b0x[a-fA-F0-9]{40}\b` | Address format |
| Stripe Secret | `sk_(?:live|test)_[A-Za-z0-9]{24,}` | Prefix check |
| Stripe Publishable | `pk_(?:live|test)_[A-Za-z0-9]{24,}` | Prefix check |

### Technical

| Pattern Name | Regex | Example Match |
|--------------|-------|---------------|
| Internal IP | `\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b` | 10.0.0.1 |
| Private Key | `-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----` | Key header |
| DB Connection | `(?:mongodb|mysql|postgres|redis):\/\/[^\s'"]+` | mongodb://user:pass@... |
| Stack Trace | `(?:at\s+[\w.$]+\s*$$[^)]+$$)|(?:Error:|Exception:)` | at Function.call (...) |

## 8.2 Security Header Analysis

### Checked Headers

| Header | Expected Value | Finding if Missing/Wrong |
|--------|---------------|-------------------------|
| `Strict-Transport-Security` | Present with max-age | Medium: Missing HSTS |
| `X-Content-Type-Options` | `nosniff` | Medium: MIME sniffing possible |
| `X-Frame-Options` | `DENY` or `SAMEORIGIN` | Medium: Clickjacking possible |
| `Content-Security-Policy` | Present | Medium: No CSP protection |
| `X-XSS-Protection` | `1; mode=block` | Low: Legacy XSS protection missing |
| `Referrer-Policy` | Present | Low: Referrer leakage possible |

### CORS Analysis

| Configuration | Severity | Finding |
|---------------|----------|---------|
| `Access-Control-Allow-Origin: *` | Medium | Wildcard CORS allows any origin |
| `*` + `Allow-Credentials: true` | High | Dangerous: credentials with wildcard |
| Reflects Origin header | Medium | Dynamic CORS may be exploitable |

## 8.3 Cookie Security

### Analyzed Attributes

| Attribute | Security Purpose | Finding if Missing |
|-----------|-----------------|-------------------|
| `Secure` | Only send over HTTPS | High: Cookie sent over HTTP |
| `HttpOnly` | Not accessible to JS | High: XSS can steal cookie |
| `SameSite` | CSRF protection | Medium: CSRF possible |
| `Path` | Limit cookie scope | Low: Overly broad path |
| `Domain` | Limit to domain | Medium: Sent to all subdomains |
| `Max-Age/Expires` | Limit lifetime | Low: Long-lived sensitive cookie |

### Sensitive Cookie Detection

Cookies with these names (case-insensitive) get extra scrutiny:
- `session`, `sess`
- `token`, `auth`
- `jwt`, `access`
- `refresh`
- `csrf`, `xsrf`
- `sid`, `ssid`

## 8.4 GraphQL Security

### Detected Issues

| Issue | Severity | Detection Method |
|-------|----------|-----------------|
| Introspection Enabled | Medium | Successful `__schema` query |
| Deep Queries (>10 levels) | High | Counting `{` nesting |
| High Complexity (>100) | Medium | Calculated score |
| Query Batching | Low | Array in request body |
| Unauthenticated Mutation | High | Mutation without auth headers |
| Sensitive Field Access | Medium | Field name matching |

### Complexity Calculation

\`\`\`
complexity = (field_count * 1) * (1 + depth * 0.5) + (fragment_count * 2)
\`\`\`

## 8.5 Rate Limit Analysis

### Detected Headers

| Header Pattern | Standard |
|----------------|----------|
| `X-RateLimit-Limit` | Common |
| `X-RateLimit-Remaining` | Common |
| `X-RateLimit-Reset` | Common |
| `RateLimit-Limit` | Draft RFC |
| `RateLimit-Remaining` | Draft RFC |
| `RateLimit-Reset` | Draft RFC |
| `RateLimit-Policy` | Draft RFC |
| `Retry-After` | HTTP Standard |

### Security Findings

| Finding | Severity | Condition |
|---------|----------|-----------|
| Rate Limit Nearly Exhausted | High | >90% used |
| Rate Limit Usage High | Medium | >75% used |
| Request Rate Limited | High | 429 status |
| Missing Rate Limit | Medium | Sensitive endpoint without headers |
| High Rate Limit | Low | Limit >10,000 |

## 8.6 Entropy-Based Detection

### How It Works

Shannon entropy measures randomness in a string. High-entropy strings often indicate secrets.

**Formula:**
\`\`\`
H = -Σ p(x) * log2(p(x))
\`\`\`

Where `p(x)` is the probability of each character.

### Detection Criteria

| Criteria | Threshold |
|----------|-----------|
| Minimum Length | 16 characters |
| Minimum Entropy | 4.5 bits |
| Maximum Length | 500 characters |

### Filtering

To reduce false positives, entropy detection:
1. Skips strings already matched by specific patterns
2. Checks for base64/hex encoding patterns
3. Requires mix of character types
4. Excludes common field names (id, name, title, etc.)

---

# 9. Export & Reporting

## 9.1 JSON Export

The default export format preserves all captured data.

### Structure

\`\`\`json
{
  "exportedAt": "2024-01-15T10:30:00.000Z",
  "version": "1.0.0",
  "tool": "Shadow API Inspector",
  "stats": {
    "totalRequests": 150,
    "uniqueDomains": 8,
    "bySeverity": {
      "critical": 2,
      "high": 5,
      "medium": 12,
      "low": 8
    }
  },
  "requests": [...],
  "findings": [...],
  "domains": [...],
  "baselines": [...]
}
\`\`\`

### Use Cases

- Full data backup
- Import into other tools
- Custom analysis scripts
- Long-term archival

## 9.2 CSV Export

Tabular format suitable for spreadsheets.

### Files Generated

The CSV export includes multiple sections:

**REQUESTS:**
\`\`\`csv
id,timestamp,method,url,status,duration,type,severity,findingsCount
req-001,2024-01-15T10:30:00Z,GET,/api/users,200,145,fetch,medium,2
\`\`\`

**FINDINGS:**
\`\`\`csv
timestamp,severity,type,description,url,location
2024-01-15T10:30:00Z,high,Authentication,JWT token detected,/api/login,responseBody
\`\`\`

**DOMAINS:**
\`\`\`csv
domain,type,requests,endpoints,methods,hasFindings,criticalCount
api.example.com,internal,47,12,GET;POST;PUT,true,1
\`\`\`

### Use Cases

- Spreadsheet analysis
- Data visualization
- Management reporting
- Compliance documentation

## 9.3 Markdown Reports

Human-readable reports suitable for documentation.

### Structure

\`\`\`markdown
# Shadow API Inspector Report

**Generated:** January 15, 2024, 10:30 AM
**Tool Version:** 1.0.0

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Requests | 150 |
| Unique Domains | 8 |
| Critical Findings | 2 |
| High Findings | 5 |

## Security Findings

### CRITICAL (2)

#### 1. AWS Access Key detected
**URL:** `/api/config`
**Location:** responseBody
**Recommendation:** Rotate key immediately...

[... continues ...]
\`\`\`

### Use Cases

- VAPT reports
- Client deliverables
- Security documentation
- GitHub/GitLab integration

## 9.4 HTML Reports

Standalone HTML report with styling.

### Features

- Dark theme matching extension UI
- Responsive layout
- Syntax highlighting
- Print-friendly
- No external dependencies

### Use Cases

- Client presentations
- Email attachments
- Standalone documentation
- Executive summaries

## 9.5 SARIF Format

Static Analysis Results Interchange Format (SARIF) for SIEM integration.

### Structure

\`\`\`json
{
  "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
  "version": "2.1.0",
  "runs": [{
    "tool": {
      "driver": {
        "name": "Shadow API Inspector",
        "version": "1.0.0",
        "rules": [...]
      }
    },
    "results": [...]
  }]
}
\`\`\`

### Compatible Tools

- GitHub Code Scanning
- Azure DevOps
- Splunk
- Elastic Security
- Microsoft Sentinel
- Many SIEM platforms

### Use Cases

- CI/CD integration
- Automated security workflows
- SIEM ingestion
- Compliance automation

---

# 10. Use Cases

## 10.1 VAPT Workflow

### Phase 1: Reconnaissance

**Objective:** Discover all API endpoints

**Steps:**
1. Install Shadow API Inspector
2. Browse the application normally for 15-30 minutes
3. Exercise all functionality (login, forms, navigation)
4. Review Domains tab for complete API surface

**Output:**
- Complete list of internal APIs
- Third-party dependencies
- Undocumented endpoints
- API versioning information

**Time Saved:** 2-3 days → 30 minutes

### Phase 2: Vulnerability Assessment

**Objective:** Identify security issues

**Steps:**
1. Review Findings tab for automatic detections
2. Analyze each critical/high finding
3. Check GraphQL tab for API-specific issues
4. Review Baselines for anomalies

**Checklist:**
- [ ] Sensitive data in responses
- [ ] Authentication token exposure
- [ ] Missing security headers
- [ ] Cookie security issues
- [ ] Rate limiting gaps
- [ ] CORS misconfigurations
- [ ] GraphQL introspection
- [ ] Third-party data leakage

### Phase 3: Active Testing

**Objective:** Validate and exploit findings

**Steps:**
1. Select suspicious request from list
2. Copy as cURL or use Replay function
3. Modify parameters for testing
4. Document results

**Integration with Other Tools:**
\`\`\`bash
# Export to Burp Suite
# Copy as cURL, import into Burp Repeater

# Export to SQLMap
# Copy request, save to file, run SQLMap
\`\`\`

### Phase 4: Reporting

**Objective:** Generate client deliverable

**Steps:**
1. Click Export → Markdown
2. Review generated report
3. Add context and recommendations
4. Include screenshots as needed

**Report Sections:**
- Executive Summary (auto-generated)
- Findings by Severity (auto-generated)
- API Inventory (auto-generated)
- Recommendations (add manually)
- Remediation Guidance (add manually)

## 10.2 SOC Monitoring

### Setup Phase

**Objective:** Establish baselines for critical applications

**Steps:**
1. Deploy extension to monitoring browser/profile
2. Navigate to critical applications
3. Let extension learn for 7-14 days
4. Lock baselines when learning complete

**Configuration:**
\`\`\`
Alert Settings:
- Critical: Immediate notification
- High: Immediate notification
- Medium: Batch notification (hourly)
- Low: Dashboard only
\`\`\`

### Monitoring Phase

**Objective:** Detect anomalies in real-time

**Watch For:**
- New endpoints called by third-party scripts
- Sudden data exfiltration spikes
- Changed response structures
- New authentication patterns
- Geographic anomalies

**Alert Response:**
1. Receive notification
2. Review in dashboard
3. Correlate with other security tools
4. Escalate if necessary

### Incident Response

**Objective:** Investigate potential compromises

**Steps:**
1. Export all data for timeframe
2. Filter by suspicious domain/pattern
3. Create timeline of events
4. Identify data exposure
5. Generate incident report

## 10.3 Bug Bounty Hunting

### Reconnaissance

**Quick Wins:**
1. Browse target application
2. Check Findings tab immediately
3. Look for:
   - Exposed API keys
   - Debug endpoints
   - Admin interfaces
   - Legacy API versions

### Hidden Endpoints

**Discovery Technique:**
1. Monitor all requests during browsing
2. Look for:
   - `/api/v1/` when app uses `/api/v2/`
   - `/admin/` or `/debug/` paths
   - Undocumented parameters
   - Mobile API endpoints

### Data Leakage

**Common Findings:**
- API returns more data than UI displays
- User data accessible without authentication
- IDOR vulnerabilities
- PII in error messages

### Authentication Bypass

**What to Look For:**
- Tokens in URL parameters
- Weak session management
- Missing authentication on endpoints
- Token reuse across domains

## 10.4 Development Security

### During Development

**Integrate into Workflow:**
1. Install extension in development browser
2. Test features as you build
3. Check for accidental data exposure
4. Verify security headers

### Pre-Production Checklist

- [ ] No debug endpoints accessible
- [ ] No unnecessary data in responses
- [ ] All security headers present
- [ ] Cookies properly secured
- [ ] Rate limiting implemented
- [ ] GraphQL introspection disabled
- [ ] No hardcoded credentials

### CI/CD Integration

**Export SARIF for Automation:**
\`\`\`bash
# After manual testing
# Export SARIF format
# Upload to CI/CD pipeline
# Fail build if critical findings
\`\`\`

---

# 11. Technical Implementation

## 11.1 Interception Techniques

### Native API Override

The primary interception method replaces native browser APIs:

\`\`\`javascript
// Store original
const originalFetch = window.fetch;

// Replace with interceptor
window.fetch = async function(...args) {
  // Pre-request processing
  const requestData = captureRequest(args);
  
  try {
    // Call original function
    const response = await originalFetch.apply(this, args);
    
    // Post-response processing
    captureResponse(response, requestData);
    
    // Return original response
    return response;
  } catch (error) {
    captureError(error, requestData);
    throw error;
  }
};
\`\`\`

**Why This Works:**
- Runs before page scripts load (`document_start`)
- Replaces API in global scope
- Page code calls our function unknowingly
- We call original, passing through results

### Script Injection

The interceptor runs in **page context**, not content script context:

\`\`\`javascript
// injector.js (content script)
const script = document.createElement('script');
script.src = chrome.runtime.getURL('content/interceptor.js');
document.documentElement.appendChild(script);
\`\`\`

**Why Two Contexts:**
- Content scripts are isolated from page
- Cannot access page's JavaScript objects
- Injection puts code in page context
- Communication via CustomEvents

### Event Communication

\`\`\`javascript
// Interceptor (page context)
window.dispatchEvent(new CustomEvent('__shadowApi_request', {
  detail: requestData
}));

// Injector (content script)
window.addEventListener('__shadowApi_request', (event) => {
  chrome.runtime.sendMessage({
    type: 'API_REQUEST',
    data: event.detail
  });
});
\`\`\`

## 11.2 Analysis Engine

### Pattern Matching

\`\`\`javascript
// For each pattern in sensitivePatterns
for (const [name, config] of Object.entries(this.sensitivePatterns)) {
  const matches = content.match(config.pattern);
  
  if (matches) {
    // Validate matches if validation function exists
    const validMatches = config.validate 
      ? matches.filter(m => config.validate(m))
      : matches;
    
    if (validMatches.length > 0) {
      findings.push({
        type: config.type,
        severity: config.severity,
        description: config.description,
        matches: validMatches.map(m => maskSensitive(m))
      });
    }
  }
}
\`\`\`

### Entropy Calculation

\`\`\`javascript
calculateEntropy(str) {
  if (!str || str.length === 0) return 0;
  
  // Count character frequencies
  const freq = {};
  for (const char of str) {
    freq[char] = (freq[char] || 0) + 1;
  }
  
  // Calculate Shannon entropy
  let entropy = 0;
  const len = str.length;
  
  for (const count of Object.values(freq)) {
    const p = count / len;
    entropy -= p * Math.log2(p);
  }
  
  return entropy;
}
\`\`\`

### Luhn Validation

\`\`\`javascript
validateLuhn(number) {
  const digits = number.replace(/\D/g, '');
  if (digits.length < 13 || digits.length > 19) return false;
  
  let sum = 0;
  let isEven = false;
  
  for (let i = digits.length - 1; i >= 0; i--) {
    let digit = parseInt(digits[i], 10);
    
    if (isEven) {
      digit *= 2;
      if (digit > 9) digit -= 9;
    }
    
    sum += digit;
    isEven = !isEven;
  }
  
  return sum % 10 === 0;
}
\`\`\`

## 11.3 Storage Strategy

### IndexedDB Schema

\`\`\`javascript
// Database: ShadowApiInspector
// Version: 1

// Object Stores:
const stores = {
  requests: {
    keyPath: 'id',
    indexes: ['timestamp', 'url', 'domain', 'severity']
  },
  settings: {
    keyPath: 'key'
  },
  baselines: {
    keyPath: 'domain'
  },
  customRules: {
    keyPath: 'name'
  }
};
\`\`\`

### Data Retention

\`\`\`javascript
async cleanupOldData() {
  const settings = await this.getSettings();
  const retentionDays = settings.retentionDays || 7;
  const cutoffDate = Date.now() - (retentionDays * 24 * 60 * 60 * 1000);
  
  const transaction = db.transaction(['requests'], 'readwrite');
  const store = transaction.objectStore('requests');
  const index = store.index('timestamp');
  
  const range = IDBKeyRange.upperBound(cutoffDate);
  const cursor = await index.openCursor(range);
  
  while (cursor) {
    cursor.delete();
    cursor.continue();
  }
}
\`\`\`

## 11.4 Performance Optimization

### Async Processing

Heavy analysis runs asynchronously to avoid blocking:

\`\`\`javascript
// Quick capture, async analysis
async processRequest(requestData) {
  // Immediately store basic data
  await this.storage.saveRequest(requestData);
  
  // Queue analysis for background processing
  this.analysisQueue.push(requestData);
  
  // Process queue in batches
  if (!this.isProcessing) {
    this.processQueue();
  }
}
\`\`\`

### Sampling High-Frequency Endpoints

\`\`\`javascript
shouldSample(url) {
  const endpointKey = this.normalizeEndpoint(url);
  const count = this.requestCounts.get(endpointKey) || 0;
  
  this.requestCounts.set(endpointKey, count + 1);
  
  // Sample after first 100 requests
  if (count > 100) {
    return count % 10 === 0; // 10% sampling
  }
  
  return true; // Always process first 100
}
\`\`\`

### Memory Management

\`\`\`javascript
// Limit in-memory request history
const MAX_MEMORY_REQUESTS = 1000;

if (this.requests.length > MAX_MEMORY_REQUESTS) {
  // Remove oldest requests from memory
  this.requests = this.requests.slice(-MAX_MEMORY_REQUESTS);
}
\`\`\`

---

# 12. Troubleshooting

## 12.1 Common Issues

### Extension Not Capturing Requests

**Symptoms:**
- Request list is empty
- No findings detected
- Console shows no interception message

**Solutions:**

1. **Check if enabled:**
   - Open popup, verify "Capture" is enabled
   - Check if domain is in ignore list

2. **Reload extension:**
   - Go to `chrome://extensions/`
   - Click reload button on Shadow API Inspector

3. **Reload page:**
   - Hard refresh: `Ctrl+Shift+R` / `Cmd+Shift+R`
   - Interceptor injects at page load

4. **Check console:**
   - Open DevTools (F12)
   - Look for `[Shadow API Inspector] Interception active`
   - If missing, extension failed to inject

### High Memory Usage

**Symptoms:**
- Browser becomes slow
- Memory warning from browser
- Extension unresponsive

**Solutions:**

1. **Reduce retention:**
   - Options → Data Retention → Reduce days

2. **Clear old data:**
   - Popup → Clear button

3. **Add to ignore list:**
   - High-frequency, low-value endpoints
   - Analytics domains

4. **Disable sampling:**
   - Options → Enable request sampling

### False Positives

**Symptoms:**
- Too many medium/low findings
- Legitimate data flagged as sensitive

**Solutions:**

1. **Review patterns:**
   - Some patterns have high false positive rates
   - Consider disabling in Options

2. **Add to allow list:**
   - Specific patterns can be allowed per domain

3. **Custom validation:**
   - Add custom patterns with stricter regex

## 12.2 Extension Not Working

### Chrome/Edge/Brave

**Developer Mode Issues:**
\`\`\`
"Manifest version 3 is required"
\`\`\`
- Ensure you're using the correct manifest.json
- Chrome 88+ required

**Permissions Issues:**
\`\`\`
"Cannot access contents of url"
\`\`\`
- Host permissions not granted
- Click extension → Allow on this site

**Service Worker Errors:**
\`\`\`
"Service worker registration failed"
\`\`\`
- Syntax error in background script
- Check chrome://extensions/ for errors

### Firefox

**Manifest Compatibility:**
\`\`\`
"Manifest version 3 not fully supported"
\`\`\`
- Use manifest.firefox.json (V2)
- Rename to manifest.json

**API Differences:**
\`\`\`
"chrome is not defined"
\`\`\`
- Firefox uses `browser.*` API
- Polyfills should handle this

## 12.3 Performance Issues

### Slow Dashboard

**Solutions:**
1. Reduce data retention period
2. Clear historical data
3. Filter to specific domain/timeframe
4. Disable auto-refresh

### Slow Page Loading

**Solutions:**
1. Add slow domains to ignore list
2. Enable request sampling
3. Reduce pattern count
4. Check for extension conflicts

## 12.4 Missing Requests

### Some Requests Not Captured

**Possible Causes:**

1. **Service Worker requests:**
   - Some SW requests bypass interception
   - Monitor SW separately if needed

2. **Pre-page-load requests:**
   - Requests before interceptor loads
   - Usually minimal, refresh catches them

3. **Iframes from different origins:**
   - Requires cross-origin permissions
   - Check manifest host_permissions

4. **Binary responses:**
   - Images, videos not fully captured
   - Shown as `[Binary: type]`

### WebSocket Messages Missing

**Possible Causes:**
1. Connection opened before extension load
2. Refresh page to capture new connections
3. Binary WebSocket frames shown as `[Binary]`

---

# 13. Advanced Topics

## 13.1 Custom Detection Rules

### YAML Format

\`\`\`yaml
# custom-rules.yaml
rules:
  - name: "Internal User ID"
    pattern: "USR-[0-9]{8}"
    type: "PII"
    severity: "medium"
    description: "Internal user identifier detected"
    
  - name: "Session Token v2"
    pattern: "sess2_[a-f0-9]{64}"
    type: "Authentication"
    severity: "high"
    description: "Session token v2 format detected"
    validate: "lengthCheck"
\`\`\`

### Adding via Options

1. Open Options page
2. Navigate to Custom Patterns
3. Click "Add Pattern"
4. Fill in required fields
5. Test with sample data
6. Save

### Programmatic Addition

\`\`\`javascript
// Via extension API
chrome.runtime.sendMessage({
  type: 'ADD_CUSTOM_PATTERN',
  pattern: {
    name: 'Custom Token',
    pattern: 'CTK_[A-Z0-9]{32}',
    type: 'Authentication',
    severity: 'critical',
    description: 'Custom token format'
  }
});
\`\`\`

## 13.2 Extending the Tool

### Adding New Analyzers

Create a new analyzer module:

\`\`\`javascript
// background/custom-analyzer.js
export class CustomAnalyzer {
  constructor() {
    this.patterns = [];
  }
  
  analyze(requestData) {
    const findings = [];
    
    // Your analysis logic
    
    return findings;
  }
}
\`\`\`

Register in service worker:

\`\`\`javascript
// background/service-worker.js
import { CustomAnalyzer } from './custom-analyzer.js';

const customAnalyzer = new CustomAnalyzer();

// In processRequest:
const customFindings = customAnalyzer.analyze(requestData);
findings.push(...customFindings);
\`\`\`

### Adding Export Formats

\`\`\`javascript
// background/export-manager.js
exportCustomFormat(data, options = {}) {
  // Transform data to your format
  const output = this.transformData(data);
  
  return {
    content: output,
    filename: `export-${this.getDateStr()}.custom`,
    mimeType: 'application/x-custom'
  };
}
\`\`\`

## 13.3 Integration with Other Tools

### Burp Suite Integration

\`\`\`bash
# Export requests as cURL
# Import into Burp Suite Repeater

# Or use Burp's API
curl -X POST "http://127.0.0.1:1337/v0.1/scan" \
  -d @shadow-api-export.json
\`\`\`

### SIEM Integration

**Splunk:**
\`\`\`
# Use SARIF export
# Configure Splunk HEC input
# Forward SARIF findings
\`\`\`

**Elastic Security:**
\`\`\`
# Export SARIF
# Use Filebeat to ingest
# Create detection rules
\`\`\`

### CI/CD Integration

**GitHub Actions:**
\`\`\`yaml
- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: shadow-api-report.sarif
\`\`\`

---

# 14. Security & Privacy

## 14.1 Data Handling

### Where Data Is Stored

| Data Type | Storage Location | Encryption |
|-----------|-----------------|------------|
| Requests | Local IndexedDB | No* |
| Settings | chrome.storage.local | No |
| Baselines | Local IndexedDB | No |
| Custom Rules | chrome.storage.local | No |

*Data is stored locally only and never transmitted.

### What Is NOT Collected

- No telemetry
- No usage analytics
- No crash reports
- No external API calls
- No cloud sync

### Data Export Security

When exporting:
- Sensitive data is partially masked by default
- Full data available with option
- User controls export destination
- No automatic uploads

## 14.2 Permissions Explained

| Permission | Purpose | Scope |
|------------|---------|-------|
| `storage` | Save settings and data | Local only |
| `tabs` | Get current tab URL | Active tab |
| `activeTab` | Interact with current page | User-initiated |
| `webRequest` | Monitor network requests | All URLs |
| `scripting` | Inject interceptor | All URLs |
| `notifications` | Desktop alerts | System |
| `clipboardWrite` | Copy to clipboard | User-initiated |
| `<all_urls>` | Access all websites | Required for interception |

### Why `<all_urls>`?

The extension needs to:
- Intercept API calls on any website
- Inject content scripts universally
- Analyze third-party domains

Without this permission, the extension cannot function.

## 14.3 Best Practices

### For Security Teams

1. **Use dedicated browser profile**
   - Separate from personal browsing
   - Clear data after assessments

2. **Review before export**
   - Check for internal data
   - Mask sensitive information

3. **Secure exports**
   - Encrypt exported files
   - Follow data handling policies

### For Individual Users

1. **Clear data regularly**
   - Use automatic cleanup
   - Manual clear after sessions

2. **Review permissions**
   - Understand what extension can access
   - Disable when not needed

3. **Keep updated**
   - Install updates promptly
   - Check for security advisories

---

# 15. Appendix

## 15.1 Complete Pattern Reference

See Section 8.1 for complete pattern documentation.

## 15.2 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+S` / `Cmd+Shift+S` | Open popup |
| `Ctrl+Shift+C` / `Cmd+Shift+C` | Toggle capture |

### Popup Shortcuts

| Shortcut | Action |
|----------|--------|
| `1-6` | Switch tabs |
| `Esc` | Close detail view |
| `Enter` | Open selected request |
| `/` | Focus search |

## 15.3 Glossary

| Term | Definition |
|------|------------|
| **API** | Application Programming Interface - how software components communicate |
| **Baseline** | Established "normal" behavior pattern for a domain |
| **CORS** | Cross-Origin Resource Sharing - browser security mechanism |
| **CSP** | Content Security Policy - HTTP header for XSS protection |
| **Entropy** | Measure of randomness in data |
| **Finding** | Detected security issue or sensitive data |
| **GraphQL** | Query language for APIs |
| **HSTS** | HTTP Strict Transport Security - forces HTTPS |
| **Interception** | Capturing API calls before they complete |
| **JWT** | JSON Web Token - authentication token format |
| **PII** | Personally Identifiable Information |
| **SARIF** | Static Analysis Results Interchange Format |
| **Shadow API** | Undocumented or hidden API endpoint |
| **SSE** | Server-Sent Events - server push technology |
| **Third-Party** | External domain/service |
| **VAPT** | Vulnerability Assessment and Penetration Testing |
| **WebSocket** | Full-duplex communication protocol |
| **XHR** | XMLHttpRequest - legacy HTTP request API |

## 15.4 Changelog

### Version 1.0.0 (Current)

**Core Features:**
- API interception (fetch, XHR, WebSocket, Beacon, SSE)
- 35+ sensitive data detection patterns
- Behavioral baselines and anomaly detection
- GraphQL analysis
- Rate limit detection
- Cookie security analysis
- Desktop notifications
- Multi-format export (JSON, CSV, Markdown, HTML, SARIF)

**Browser Support:**
- Chrome 88+
- Edge 88+
- Brave
- Firefox 109+

---

# Acknowledgments

Shadow API Inspector was designed to address critical gaps in modern web application security testing. Special thanks to the security research community for identifying the need for better client-side visibility tools.

---

# License

MIT License

Copyright (c) 2024 Shadow Security

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

**End of Documentation**

*Shadow API Inspector v1.0.0*
*Documentation Version: 1.0*
*Last Updated: November 2024*

```
