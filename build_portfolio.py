import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rahul Pal | Python Developer</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
    <script>
        // ─── EmailJS Configuration ──────────────────────────────────────────────
        const EMAILJS_PUBLIC_KEY  = "OmtHWvvABccQ8lE5L";
        const EMAILJS_SERVICE_ID  = "service_xlzdc8v";
        const EMAILJS_TEMPLATE_ID = "template_4qno77j";
        // ───────────────────────────────────────────────────────────────────────

        (function() {
            emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
        })();
    </script>
    <style>
        *, *::before, *::after {
            box-sizing: border-box;
        }
        html, body {
            overflow-x: hidden;
            overflow-y: auto !important;
            height: 100%;
            background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
            color: #0f172a;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
        }
        .code-font {
            font-family: 'Consolas', 'Courier New', monospace;
        }
        
        .fixed-portal-header {
            background: #090d16 !important;
            color: #10b981 !important;
            border: 2px solid #10b981 !important;
            box-shadow: 0 10px 40px rgba(16, 185, 129, 0.25);
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 10px 40px -10px rgba(15, 23, 42, 0.06);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .glass-card:hover {
            background: rgba(255, 255, 255, 0.80);
            border: 1px solid rgba(255, 255, 255, 0.95);
            box-shadow: 0 20px 50px -15px rgba(15, 23, 42, 0.15);
            transform: translateY(-4px);
        }
        
        .pure-terminal {
            background: #090d16 !important;
            color: #10b981 !important;
            border: 2px solid #10b981 !important;
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.35);
            animation: terminalGlowPulse 2.5s infinite ease-in-out;
        }
        @keyframes terminalGlowPulse {
            0%, 100% { box-shadow: 0 0 20px rgba(16, 185, 129, 0.2); border-color: #10b981; }
            50% { box-shadow: 0 0 35px rgba(16, 185, 129, 0.6); border-color: #34d399; }
        }

        .avatar-glow {
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.25);
            border: 4px solid rgba(255, 255, 255, 1);
            transition: all 0.4s ease;
        }
        .glass-card:hover .avatar-glow {
            box-shadow: 0 0 35px rgba(59, 130, 246, 0.45);
            transform: scale(1.03);
        }
        .modal-overlay {
            background: rgba(2, 6, 23, 0.8);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }
        .accent-bar {
            height: 4px;
            width: 100%;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6, #10b981);
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        
        .terminal-link-bar {
            background: #090d16 !important;
            border: 1px solid #10b981 !important;
            transition: all 0.2s ease-in-out;
        }
        .terminal-link-bar:hover {
            border-color: #34d399 !important;
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.3);
        }
        
        .cyber-flash-action {
            animation: brightTextFlashing 1.4s infinite ease-in-out;
        }
        @keyframes brightTextFlashing {
            0%, 100% { color: #10b981; text-shadow: 0 0 2px rgba(16, 185, 129, 0.2); }
            50% { color: #34d399; text-shadow: 0 0 12px rgba(52, 211, 153, 0.85); }
        }

        .macos-icon-btn {
            background: #ffffff !important;
            border: 1px solid rgba(15, 23, 42, 0.15);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .macos-icon-btn:hover {
            border-color: rgba(15, 23, 42, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        }

        .terminal-input-field {
            background: rgba(9, 13, 22, 0.6) !important;
            border: 1px solid #10b981 !important;
            color: #34d399 !important;
            outline: none !important;
        }
        .terminal-input-field:focus {
            border-color: #34d399 !important;
            box-shadow: 0 0 8px rgba(52, 211, 153, 0.4);
        }
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
</head>
<body class="p-4 md:p-8 tracking-wide">

    <div class="max-w-6xl mx-auto pb-6">
        <header class="fixed-portal-header p-4 rounded-lg flex justify-between items-center code-font text-sm shadow-xl">
            <div class="flex items-center space-x-2">
                <span class="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-yellow-500 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-green-500 inline-block"></span>
                <span class="font-bold ml-2 text-slate-200">rahul_pal@software_dev:~</span>
            </div>
            <div class="text-xs text-emerald-400 font-bold hidden sm:flex items-center space-x-2 animate-pulse">
                <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
                <span>SYSTEM_STATUS: ONLINE</span>
            </div>
        </header>
    </div>

    <main class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch pb-12">
        
        <section class="lg:col-span-1 flex flex-col justify-between space-y-8">
            <div class="glass-card rounded-xl relative overflow-hidden flex flex-col items-center text-center p-6 flex-1 justify-center">
                <div class="accent-bar absolute top-0 left-0"></div>
                <div class="relative w-32 h-32 mb-4 mt-2">
                    <img src="profile.png" onerror="this.src='profile.jpeg'; this.onerror=function(){this.src='https://images.unsplash.com/photo-1618401471353-b98aedd07871?q=80&w=250&auto=format&fit=crop';};" alt="Rahul Pal" class="w-full h-full rounded-full object-cover avatar-glow">
                </div>
                <h1 class="text-2xl font-extrabold text-slate-900 tracking-tight">RAHUL PAL</h1>
                <p class="text-[11px] font-bold text-blue-600 mt-1 uppercase tracking-widest code-font">Software Development Engineer</p>
                <p class="text-xs text-slate-500 font-bold flex items-center mt-1">
                    <i class="fa-solid fa-location-dot mr-1.5 text-red-500"></i>Mumbai, India
                </p>
                
                <p class="text-xs text-slate-600 mt-4 leading-relaxed text-left font-normal">
                    Backend Engineer with ~2 years of professional expertise designing production-grade web architectures, robust REST APIs, and automated processing pipelines.
                </p>
                
                <div class="mt-6 pt-4 border-t border-slate-200/80 w-full flex flex-wrap justify-center items-center gap-3">
                    <button onclick="openTerminalModal('phone')" class="macos-icon-btn p-2 rounded-lg cursor-pointer flex items-center justify-center w-9 h-9 text-base" title="View Contact Parameters">
                        <i class="fa-solid fa-phone" style="color: #10b981;"></i>
                    </button>
                    <button onclick="openTerminalModal('email')" class="macos-icon-btn p-2 rounded-lg cursor-pointer flex items-center justify-center w-9 h-9 text-base" title="Compose Secure Message">
                        <i class="fa-solid fa-envelope" style="color: #ea4335;"></i>
                    </button>
                    <a href="https://www.linkedin.com/in/rahulpal1991/" target="_blank" class="macos-icon-btn p-2 rounded-lg flex items-center justify-center w-9 h-9 text-base" title="LinkedIn Profile">
                        <i class="fa-brands fa-linkedin-in" style="color: #0077b5;"></i>
                    </a>
                    <a href="https://github.com/coderpal" target="_blank" class="macos-icon-btn p-2 rounded-lg flex items-center justify-center w-9 h-9 text-base" title="GitHub Core Hub">
                        <i class="fa-brands fa-github" style="color: #151b23;"></i>
                    </a>
                    <a href="https://leetcode.com/u/rahulpal91/" target="_blank" class="bg-white border border-slate-200/60 shadow-sm hover:shadow px-3 py-2 rounded-lg text-slate-800 flex items-center space-x-2 h-9 transition-transform hover:-translate-y-0.5" title="LeetCode Profile">
                        <i class="fa-solid fa-code text-[#d97706]"></i>
                        <span class="text-xs font-bold font-sans tracking-wide">LeetCode</span>
                    </a>
                    <a href="RahulPal.pdf" target="_blank" class="bg-white border border-slate-200/60 shadow-sm hover:shadow px-3 py-2 rounded-lg text-slate-800 flex items-center space-x-2 h-9 transition-transform hover:-translate-y-0.5" title="Download Resume">
                        <i class="fa-solid fa-download text-blue-600"></i>
                        <span class="text-xs font-bold font-sans tracking-wide">Resume</span>
                    </a>
                </div>
            </div>

            <div class="glass-card rounded-xl relative overflow-hidden p-5 flex-1 flex flex-col justify-between">
                <div class="accent-bar absolute top-0 left-0"></div>
                <h3 class="text-xs font-bold text-slate-500 mb-2 uppercase tracking-widest code-font">// TECHNICAL_SKILLS_MATRIX</h3>
                <div class="space-y-3 text-xs code-font flex-1 justify-center flex flex-col">
                    <div class="p-2.5 rounded bg-white/40 border border-white/60">
                        <span class="text-red-600 font-bold">[Languages]:</span>
                        <p class="text-slate-800 font-bold mt-0.5">Python, SQL</p>
                    </div>
                    <div class="p-2.5 rounded bg-white/40 border border-white/60">
                        <span class="text-red-600 font-bold">[Computer Science Fundamentals]:</span>
                        <p class="text-slate-800 font-bold mt-0.5">OOP, DSA, System Design</p>
                    </div>
                    <div class="p-2.5 rounded bg-white/40 border border-white/60">
                        <span class="text-red-600 font-bold">[Frameworks & Libraries]:</span>
                        <p class="text-slate-800 font-bold mt-0.5">FastAPI, Django, Streamlit</p>
                    </div>
                    <div class="p-2.5 rounded bg-white/40 border border-white/60">
                        <span class="text-red-600 font-bold">[Databases & Core Architecture]:</span>
                        <p class="text-slate-800 font-bold mt-0.5">PostgreSQL, Relational Schema Modeling</p>
                    </div>
                    <div class="p-2.5 rounded bg-white/40 border border-white/60">
                        <span class="text-red-600 font-bold">[APIs & Security Architecture]:</span>
                        <p class="text-slate-800 font-bold mt-0.5">REST API Design, JWT Authentication</p>
                    </div>
                    <div class="p-2.5 rounded bg-white/40 border border-white/60">
                        <span class="text-red-600 font-bold">[Operations, Tooling & Analytics]:</span>
                        <p class="text-slate-800 font-bold mt-0.5">Pandas, NumPy, Power BI</p>
                    </div>
                </div>
            </div>

            <div class="glass-card rounded-xl relative overflow-hidden p-5">
                <div class="accent-bar absolute top-0 left-0"></div>
                <h3 class="text-xs font-bold text-slate-500 mb-3 uppercase tracking-widest code-font">// VERIFIED_BENCHMARKS</h3>
                <ul class="text-xs code-font space-y-2.5 text-slate-800 font-bold">
                    <li class="flex items-center text-emerald-700">✓ Professional Scrum Master I (PSM I)</li>
                    <li class="flex items-center text-blue-700">⚡ IBM Generative AI Specialist (In Progress)</li>
                </ul>
            </div>
        </section>

        <section class="lg:col-span-2">
            <div class="glass-card rounded-xl relative overflow-hidden p-6 space-y-5 h-full flex flex-col justify-between">
                <div class="accent-bar absolute top-0 left-0"></div>
                
                <div>
                    <h2 class="text-lg font-extrabold text-slate-900 tracking-tight uppercase mb-4">1. Professional Experience</h2>
                    <div class="flex justify-between items-center flex-wrap gap-2 mb-3">
                        <p class="text-sm text-slate-700 font-bold">
                            Web Application Developer — <span class="text-blue-600">Kalki Fashion Pvt. Ltd.</span>
                        </p>
                        <span class="text-xs font-bold text-blue-600 bg-blue-50/80 border border-blue-200/60 px-2.5 py-1 rounded-full code-font">
                            Apr 2024 - Jan 2026
                        </span>
                    </div>
                </div>

                <div class="p-4 bg-white/80 border-l-4 border-l-purple-600 border-y-slate-200/60 border-r-slate-200/60 border rounded-r-lg shadow-sm space-y-3 hover:border-purple-300/80 transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center flex-wrap gap-2 mb-2">
                            <h3 class="text-sm font-bold text-purple-600 code-font">[System-A]: Order-to-Dispatch Ecosystem</h3>
                            <span class="bg-blue-100 text-blue-700 px-2.5 py-0.5 rounded-full text-[10px] font-bold code-font">FastAPI // Django ORM // PostgreSQL</span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed font-medium">
                            Architected and deployed a transactional, full-stack Order-to-Dispatch platform covering operations from tracking order entry up to warehouse physical routing. Designed structured relational database schemas using Django ORM-style modeling patterns to completely eliminate manual tracing and map real-time workflows.
                        </p>
                        <ul class="text-xs text-slate-700 font-bold list-disc pl-4 space-y-1 mt-2">
                            <li>Reduced end-to-end order processing latency by <span class="text-blue-600">40%</span> across internal channels.</li>
                            <li>Achieved <span class="text-emerald-600">100% adoption</span> across all operational teams within the first month of production deployment.</li>
                            <li>Secured all operational endpoints by configuring stateful JWT-based cryptographic token claims.</li>
                        </ul>
                    </div>
                    
                    <button onclick="openTerminalModal('dispatch')" class="w-full terminal-link-bar rounded-md font-mono text-xs p-2.5 mt-2 shadow-none cursor-pointer flex justify-between items-center tracking-wide group">
                        <span class="text-yellow-400 font-bold text-left">> Run Telemetry Diagnostics <span class="text-slate-500 font-normal">[API_GATEWAY]</span></span>
                        <span class="cyber-flash-action font-bold text-right group-hover:underline">Click Here 👈</span>
                    </button>
                </div>

                <div class="p-4 bg-white/80 border-l-4 border-l-purple-600 border-y-slate-200/60 border-r-slate-200/60 border rounded-r-lg shadow-sm space-y-3 hover:border-purple-300/80 transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center flex-wrap gap-2 mb-2">
                            <h3 class="text-sm font-bold text-purple-600 code-font">[System-B]: Inventory Management System</h3>
                            <span class="bg-blue-100 text-blue-700 px-2.5 py-0.5 rounded-full text-[10px] font-bold code-font">FastAPI // PostgreSQL</span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed font-medium">
                            Engineered and built a high-availability, multi-user inventory tracking cluster engineered reliably on MySQL backend storage tiers to scale seamlessly without concurrency degradation mutations.
                        </p>
                        <ul class="text-xs text-slate-700 font-bold list-disc pl-4 space-y-1 mt-2">
                            <li>Safely supported <span class="text-blue-600">150+ concurrent corporate users</span> without resource degradation locks.</li>
                            <li>Cut data synchronization and internal fulfillment process errors down by <span class="text-emerald-600">50%</span>.</li>
                            <li>Integrated explicit role-based system access controls, dynamic stock tracking vectors, and reactive automated reorder triggers.</li>
                        </ul>
                    </div>
                    
                    <button onclick="openTerminalModal('inventory')" class="w-full terminal-link-bar rounded-md font-mono text-xs p-2.5 mt-2 shadow-none cursor-pointer flex justify-between items-center tracking-wide group">
                        <span class="text-yellow-400 font-bold text-left">> Trace Concurrency Assertions <span class="text-slate-500 font-normal">[MUTEX_LOCK_POOL]</span></span>
                        <span class="cyber-flash-action font-bold text-right group-hover:underline">Click Here 👈</span>
                    </button>
                </div>

                <div class="p-4 bg-white/80 border-l-4 border-l-purple-600 border-y-slate-200/60 border-r-slate-200/60 border rounded-r-lg shadow-sm space-y-3 hover:border-purple-300/80 transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center flex-wrap gap-2 mb-2">
                            <h3 class="text-sm font-bold text-purple-600 code-font">[System-C]: ETL & BI Pipeline</h3>
                            <span class="bg-blue-100 text-blue-700 px-2.5 py-0.5 rounded-full text-[10px] font-bold code-font">Pandas // NumPy // Google Sheets API // Power BI</span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed font-medium">
                            Automated structural bi-directional data synchronisation across heterogeneous files, live Excel frames, and relational MySQL instances using custom processing scripts, completely eliminating manual ledger reconciliation passes.
                        </p>
                        <ul class="text-xs text-slate-700 font-bold list-disc pl-4 space-y-1 mt-2">
                            <li>Executed vector manipulation and math data transformations utilizing Pandas dataframes and NumPy matrices.</li>
                            <li>Generated centralized, fully audit-ready data sources across multiple business reporting pipelines.</li>
                            <li>Built real-time executive Power BI dashboards powered by continuous API streaming to heighten executive supply chain visibility.</li>
                        </ul>
                    </div>
                    
                    <button onclick="openTerminalModal('pipeline')" class="w-full terminal-link-bar rounded-md font-mono text-xs p-2.5 mt-2 shadow-none cursor-pointer flex justify-between items-center tracking-wide group">
                        <span class="text-yellow-400 font-bold text-left">> Run Serialization Traces <span class="text-slate-500 font-normal">[DATA_STREAM_ETL]</span></span>
                        <span class="cyber-flash-action font-bold text-right group-hover:underline">Click Here 👈</span>
                    </button>
                </div>

                <div class="text-[10px] text-slate-400 code-font italic px-1 pt-1 border-t border-slate-200/60">
                    * Compliance Alert: Diagnostics simulate architectural schema mutations and validation routines. Exact source strings are obfuscated to preserve corporate intellectual property (IP).
                </div>
            </div>
        </section>
        
        <section class="lg:col-span-3 space-y-8">
            <div class="glass-card rounded-xl relative overflow-hidden p-6 space-y-4">
                <div class="accent-bar absolute top-0 left-0"></div>
                <div class="flex justify-between items-center">
                    <h2 class="text-lg font-extrabold text-slate-900 tracking-tight uppercase">2. Cloud Architecture Projects</h2>
                    <span class="text-[10px] bg-blue-600 text-white font-bold px-2.5 py-1 rounded-full code-font shadow-sm shadow-blue-500/20">Streamlit Live Hub</span>
                </div>
                
                <div class="p-4 bg-white/80 border border-slate-200/60 rounded-lg space-y-3 shadow-sm">
                    <h4 class="text-sm font-bold text-slate-800 code-font flex items-center">
                        <span class="w-2 h-2 rounded-full bg-blue-500 inline-block mr-2"></span>
                        Exchange-Style Market Surveillance Dashboard
                    </h4>
                    <p class="text-xs text-slate-600 leading-relaxed font-medium">
                        An advanced cloud-based market infrastructure analytics platform replicating exchange risk management mechanisms. Automated real-time NSE Bhavcopy ingestion passes coupled with custom multi-variable volatility, systemic liquidity shocks, and trading anomaly alert scoring conditions.
                    </p>
                    <div class="inline-block">
                        <span class="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-[11px] font-bold code-font">
                            Python // Pandas // NumPy // PostgreSQL Cloud Infrastructure // Streamlit Server Engine
                        </span>
                    </div>
                    <div class="pt-1 flex space-x-4 text-xs code-font font-bold">
                        <a href="https://nse-surveillance.streamlit.app" target="_blank" class="text-blue-600 hover:text-blue-700 flex items-center space-x-1">
                            <i class="fa-solid fa-arrow-up-right-from-square"></i>
                            <span>Launch Live App Console</span>
                        </a>
                        <a href="https://github.com/coderpal/exchange-surveillance-console" target="_blank" class="text-slate-500 hover:text-slate-700 flex items-center space-x-1">
                            <i class="fa-brands fa-git-alt"></i>
                            <span>Core Git Codebase</span>
                        </a>
                    </div>
                </div>
            </div>

            <div class="glass-card rounded-xl relative overflow-hidden p-6 space-y-4">
                <div class="accent-bar absolute top-0 left-0"></div>
                <div class="flex justify-between items-center flex-wrap gap-2">
                    <h2 class="text-lg font-extrabold text-slate-900 tracking-tight uppercase">3. Interactive DSA Runtime Benchmark</h2>
                    <span class="text-[10px] bg-emerald-600 text-white font-bold px-2.5 py-1 rounded-full code-font shadow-sm shadow-emerald-500/20">In-Browser JS Visualizer</span>
                </div>
                <p class="text-xs text-slate-600 leading-relaxed font-medium">
                    Execute an active multi-pointer QuickSort routine inside the DOM canvas box below to verify real-time mutations and data structural sorting step metrics in worst/average case operational paradigms <span class="font-bold text-blue-600 code-font">O(N log N)</span>.
                </p>

                <div class="bg-slate-950 h-36 w-full rounded-lg border border-slate-800 flex items-end justify-between p-3 space-x-1 shadow-[0_0_20px_rgba(16,185,129,0.05)]" id="sorting-array-canvas"></div>

                <div class="mt-4 flex flex-wrap gap-4 justify-between items-center">
                    <div class="flex space-x-2">
                        <button onclick="createNewStateArray()" class="bg-white border border-slate-200 text-xs text-slate-700 px-3 py-2 rounded-md font-bold hover:bg-slate-50 hover:border-slate-300 active:scale-95 transition-all shadow-sm cursor-pointer">Generate Random State</button>
                        <button onclick="executeQuickSortEngine()" class="bg-emerald-600 text-xs text-white px-3 py-2 rounded-md font-bold hover:bg-emerald-700 active:scale-95 transition-all shadow-sm cursor-pointer">Execute QuickSort</button>
                    </div>
                    <div class="text-xs code-font font-bold text-slate-700 bg-white/80 border border-slate-200 px-3 py-1.5 rounded-md shadow-sm" id="sorting-metrics-board">
                        Time: <span class="text-blue-600">Ready</span> | Swaps: <span class="text-blue-600">0</span>
                    </div>
                </div>
                
                <div class="text-[11px] text-slate-500 code-font mt-2 border-t border-slate-200 pt-2 leading-relaxed">
                    * Computational Note: This module visually breaks down the divide-and-conquer paradigm. It selects the rightmost element as a pivot, partitions the array by moving smaller items to the left, and recursively sorts sub-segments in real-time. <strong><br>[Rationale Component]: This engine is embedded to showcase mathematical scalability optimizations, low-level operational flow monitoring, and memory-space complexity assertion handling natively within rendering execution scopes.</strong>
                </div>
            </div>
        </section>
    </main>

    <div id="terminal-modal" class="fixed inset-0 modal-overlay z-50 flex items-center justify-center hidden p-4">
        <div class="w-full max-w-2xl pure-terminal rounded-xl overflow-hidden flex flex-col transform transition-all duration-300">
            <div class="bg-slate-950 border-b border-emerald-950/60 px-4 py-3 flex justify-between items-center">
                <div class="flex items-center space-x-2">
                    <button onclick="closeTerminalModal()" class="w-3 h-3 rounded-full bg-red-500 inline-block hover:bg-red-600 transition-colors cursor-pointer" title="Close Window"></button>
                    <span class="w-3 h-3 rounded-full bg-yellow-500 inline-block"></span>
                    <span class="w-3 h-3 rounded-full bg-green-500 inline-block"></span>
                    <span class="text-xs text-slate-400 code-font font-bold ml-2" id="modal-terminal-title">
                        telemetry_trace.sh
                    </span>
                </div>
                <div class="text-[10px] text-slate-500 code-font tracking-wider bg-slate-900 px-2 py-0.5 rounded">
                    ESC to exit
                </div>
            </div>
            <div class="p-5 code-font text-xs overflow-y-auto max-h-[470px] leading-relaxed tracking-wide bg-slate-950/95 text-emerald-400" id="modal-terminal-body">
                // Hydrating metrics sequences...
            </div>
        </div>
    </div>

    <footer class="max-w-6xl mx-auto p-6 text-center text-xs text-slate-500 code-font border-t border-slate-300/40 mb-4">
        portfolio/build_portfolio.py // Static Server Assembly Frame // Generated via pure automated engine components.
    </footer>

    <script>
        // EmailJS-powered in-browser email dispatch — no server, no redirects
        async function dispatchClientEmailStream(event) {
            if(event) event.preventDefault();

            const sendButton = document.getElementById('mac-send-btn') || document.getElementById('smtp-submit-btn');
            const statusLabel = document.getElementById('smtp-status-log');

            const senderRef = document.getElementById('smtp-sender-input')?.value.trim();
            const subjectRef = document.getElementById('smtp-subject-input')?.value.trim();
            // Read from contenteditable editor; strip to plain text for EmailJS
            const bodyEditor = document.getElementById('mac-body-editor');
            const bodyHtml = bodyEditor ? bodyEditor.innerHTML.trim() : '';
            const bodyRef = bodyEditor ? bodyEditor.innerText.trim() : '';

            if(!senderRef || !subjectRef || !bodyRef) {
                if(statusLabel) {
                    statusLabel.innerHTML = "Please fill in all required fields.";
                    statusLabel.style.color = "#ff3b30";
                }
                return;
            }

            if(sendButton) { sendButton.disabled = true; sendButton.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="animation:spin 1s linear infinite"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg> Sending…`; }
            if(statusLabel) { statusLabel.innerHTML = "Sending your message…"; statusLabel.style.color = "#f5a623"; }

            const templateParams = {
                name:    senderRef,
                email:   senderRef,
                subject: subjectRef,
                message: bodyRef,
            };

            try {
                await emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, templateParams);
                executeSuccessUI(statusLabel, sendButton);
            } catch (error) {
                console.error("EmailJS dispatch error:", error);
                if(statusLabel) { statusLabel.innerHTML = "Failed to send. Please try again."; statusLabel.style.color = "#ff3b30"; }
                if(sendButton) {
                    sendButton.disabled = false;
                    sendButton.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg> Send E-Mail`;
                }
            }
        }

        function executeSuccessUI(statusLabel, sendButton) {
            if(statusLabel) { statusLabel.innerHTML = "Message sent successfully!"; statusLabel.style.color = "#34c759"; }
            if(sendButton) sendButton.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Sent!`;
            // Show macOS success dialog on top of the compose window
            showMacDialog();
        }

        function showMacDialog() {
            const overlay = document.createElement('div');
            overlay.id = 'mac-overlay';
            overlay.style.cssText = 'position:fixed;inset:0;z-index:10000;display:flex;align-items:center;justify-content:center;';

            overlay.innerHTML = `
                <div id="mac-dialog" style="
                    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', sans-serif;
                    background: rgba(235,235,235,0.96);
                    backdrop-filter: blur(40px);
                    -webkit-backdrop-filter: blur(40px);
                    border-radius: 12px;
                    width: 300px;
                    box-shadow: 0 22px 70px rgba(0,0,0,0.45), 0 0 0 0.5px rgba(0,0,0,0.18);
                    overflow: hidden;
                    animation: macPop 0.18s cubic-bezier(0.34,1.56,0.64,1);
                ">
                    <style>
                        @keyframes macPop {
                            from { transform: scale(0.82); opacity: 0; }
                            to   { transform: scale(1);    opacity: 1; }
                        }
                    </style>

                    <!-- Title bar with traffic lights -->
                    <div style="
                        background: linear-gradient(180deg, #e8e8e8 0%, #d8d8d8 100%);
                        border-bottom: 1px solid #c0c0c0;
                        padding: 10px 12px 9px;
                        display: flex;
                        align-items: center;
                        gap: 8px;
                        position: relative;
                    ">
                        <!-- Close button (red) -->
                        <button onclick="closeMacDialog()" id="mac-close-btn" style="
                            width:13px;height:13px;border-radius:50%;
                            background:#ff5f57;border:0.5px solid #e0443e;
                            cursor:pointer;display:flex;align-items:center;justify-content:center;
                            font-size:8px;color:transparent;transition:color 0.1s;flex-shrink:0;
                        " onmouseover="this.style.color='#7a0000'" onmouseout="this.style.color='transparent'">✕</button>
                        <!-- Minimise (yellow, decorative) -->
                        <div style="width:13px;height:13px;border-radius:50%;background:#febc2e;border:0.5px solid #d9a325;flex-shrink:0;"></div>
                        <!-- Maximise (green, decorative) -->
                        <div style="width:13px;height:13px;border-radius:50%;background:#28c840;border:0.5px solid #1aab2e;flex-shrink:0;"></div>

                        <span style="
                            position:absolute;left:50%;transform:translateX(-50%);
                            font-size:12px;font-weight:600;color:#3a3a3a;letter-spacing:-0.1px;
                        ">Mail</span>
                    </div>

                    <!-- Body -->
                    <div style="padding:22px 20px 10px;text-align:center;">
                        <div style="font-size:36px;margin-bottom:10px;">✉️</div>
                        <div style="font-size:14px;font-weight:600;color:#1a1a1a;margin-bottom:5px;letter-spacing:-0.2px;">Sent Successfully</div>
                        <div style="font-size:12px;color:#666;line-height:1.5;">Your message has been delivered to Rahul.</div>
                    </div>

                    <!-- Countdown -->
                    <div style="text-align:center;padding:4px 0 2px;">
                        <span id="mac-countdown" style="font-size:10px;color:#aaa;letter-spacing:0.1px;">Closing in 5s</span>
                    </div>

                    <!-- OK button -->
                    <div style="padding:12px 20px 18px;display:flex;justify-content:center;">
                        <button onclick="closeMacDialog()" id="mac-ok-btn" style="
                            background: linear-gradient(180deg, #34c759 0%, #28a745 100%);
                            border: none;
                            border-radius: 6px;
                            color: #fff;
                            font-size: 13px;
                            font-weight: 600;
                            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                            padding: 5px 0;
                            width: 100%;
                            cursor: pointer;
                            box-shadow: 0 1px 3px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.25);
                            letter-spacing: -0.1px;
                            transition: filter 0.1s;
                        " onmouseover="this.style.filter='brightness(1.08)'" onmouseout="this.style.filter='brightness(1)'">OK</button>
                    </div>
                </div>
            `;

            document.body.appendChild(overlay);
            setTimeout(() => document.getElementById('mac-ok-btn')?.focus(), 50);

            // ESC closes mac dialog → then after 3s closes email modal
            function handleEsc(e) {
                if(e.key === 'Escape') {
                    closeMacDialog();
                    document.removeEventListener('keydown', handleEsc);
                }
            }
            document.addEventListener('keydown', handleEsc);
            overlay._escHandler = handleEsc;

            // Countdown — 5s then close mac dialog, then 3s close email modal
            let secs = 5;
            const countdownEl = document.getElementById('mac-countdown');
            const timer = setInterval(() => {
                secs--;
                if(countdownEl) countdownEl.textContent = 'Closing in ' + secs + 's';
                if(secs <= 0) { clearInterval(timer); closeMacDialog(); }
            }, 1000);
            overlay._timer = timer;
        }

        function closeMacDialog() {
            const overlay = document.getElementById('mac-overlay');
            if(!overlay) return;
            clearInterval(overlay._timer);
            document.removeEventListener('keydown', overlay._escHandler);
            const dialog = document.getElementById('mac-dialog');
            if(dialog) {
                dialog.style.transition = 'transform 0.15s ease-in,opacity 0.15s ease-in';
                dialog.style.transform = 'scale(0.88)';
                dialog.style.opacity = '0';
            }
            setTimeout(() => {
                overlay.remove();
                // Close compose window after 3 more seconds (8s total)
                let secs = 3;
                const t = setInterval(() => {
                    secs--;
                    if(secs <= 0) { clearInterval(t); closeMacMailCompose(); }
                }, 1000);
                function handleEmailEsc(e) {
                    if(e.key === 'Escape') { clearInterval(t); closeMacMailCompose(); document.removeEventListener('keydown', handleEmailEsc); }
                }
                document.addEventListener('keydown', handleEmailEsc);
            }, 160);
        }

        // ── macOS Contact Card ───────────────────────────────────────────────────
        function openMacContactCard() {
            if(document.getElementById('mac-contact-card')) return;
            document.body.style.overflow = 'hidden';

            const win = document.createElement('div');
            win.id = 'mac-contact-card';
            win.style.cssText = `
                position:fixed;inset:0;z-index:9000;display:flex;align-items:center;justify-content:center;
                background:rgba(0,0,0,0.45);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);
            `;

            win.innerHTML = `
                <div id="mac-contact-window" style="
                    font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Helvetica Neue',sans-serif;
                    width:min(360px,92vw);
                    background:rgba(242,242,247,0.97);
                    backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
                    border-radius:14px;
                    box-shadow:0 30px 90px rgba(0,0,0,0.5),0 0 0 0.5px rgba(0,0,0,0.2);
                    overflow:hidden;
                    animation:macWinPop 0.2s cubic-bezier(0.34,1.46,0.64,1);
                ">
                    <!-- Title bar -->
                    <div style="background:linear-gradient(180deg,#e4e4e4 0%,#d6d6d6 100%);border-bottom:1px solid #bbb;padding:11px 14px 10px;display:flex;align-items:center;position:relative;">
                        <div style="display:flex;gap:8px;z-index:1;">
                            <button onclick="closeMacContactCard()" style="width:13px;height:13px;border-radius:50%;background:#ff5f57;border:0.5px solid #e0443e;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:7px;color:transparent;transition:color 0.1s;" onmouseover="this.style.color='#7a0000'" onmouseout="this.style.color='transparent'">✕</button>
                            <div style="width:13px;height:13px;border-radius:50%;background:#febc2e;border:0.5px solid #d9a325;"></div>
                            <div style="width:13px;height:13px;border-radius:50%;background:#28c840;border:0.5px solid #1aab2e;"></div>
                        </div>
                        <span style="position:absolute;left:50%;transform:translateX(-50%);font-size:13px;font-weight:600;color:#2a2a2a;letter-spacing:-0.15px;">Contact</span>
                    </div>

                    <!-- Avatar + name -->
                    <div style="background:linear-gradient(180deg,#e8eaf0 0%,#f2f2f7 100%);padding:28px 20px 20px;text-align:center;border-bottom:1px solid rgba(0,0,0,0.08);">
                        <div style="width:72px;height:72px;border-radius:50%;margin:0 auto 12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.18);border:2.5px solid #fff;">
                            <img src="profile.png" onerror="this.src='profile.jpeg';this.onerror=function(){this.style.display='none';this.parentElement.style.background='#3b82f6';this.parentElement.innerHTML='<span style=\\'color:#fff;font-size:28px;font-weight:700;line-height:72px;\\'>R</span>';};" style="width:100%;height:100%;object-fit:cover;">
                        </div>
                        <div style="font-size:18px;font-weight:700;color:#1a1a1a;letter-spacing:-0.3px;">Rahul Pal</div>
                        <div style="font-size:12px;color:#888;margin-top:3px;">Software Development Engineer</div>
                        <div style="font-size:12px;color:#888;margin-top:1px;">📍 Mumbai, India</div>
                    </div>

                    <!-- Contact rows -->
                    <div style="padding:8px 0;">

                        <!-- Phone -->
                        <div style="display:flex;align-items:center;padding:11px 18px;border-bottom:1px solid rgba(0,0,0,0.06);">
                            <div style="width:34px;height:34px;border-radius:8px;background:#34c759;display:flex;align-items:center;justify-content:center;margin-right:13px;flex-shrink:0;box-shadow:0 2px 6px rgba(52,199,89,0.35);">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>
                            </div>
                            <div style="flex:1;">
                                <div style="font-size:11px;color:#888;margin-bottom:1px;">mobile</div>
                                <div style="font-size:14px;color:#1a1a1a;font-weight:500;">+91 74002 08221</div>
                            </div>
                            <a href="tel:+917400208221" style="font-size:12px;color:#007aff;text-decoration:none;font-weight:500;background:rgba(0,122,255,0.1);padding:4px 10px;border-radius:6px;">Call</a>
                        </div>

                        <!-- WhatsApp -->
                        <div style="display:flex;align-items:center;padding:11px 18px;border-bottom:1px solid rgba(0,0,0,0.06);">
                            <div style="width:34px;height:34px;border-radius:8px;background:#25d366;display:flex;align-items:center;justify-content:center;margin-right:13px;flex-shrink:0;box-shadow:0 2px 6px rgba(37,211,102,0.35);">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                            </div>
                            <div style="flex:1;">
                                <div style="font-size:11px;color:#888;margin-bottom:1px;">WhatsApp</div>
                                <div style="font-size:14px;color:#1a1a1a;font-weight:500;">+91 74002 08221</div>
                            </div>
                            <a href="https://wa.me/917400208221" target="_blank" style="font-size:12px;color:#25d366;text-decoration:none;font-weight:600;background:rgba(37,211,102,0.12);padding:4px 10px;border-radius:6px;">Message</a>
                        </div>

                        <!-- Telegram -->
                        <div style="display:flex;align-items:center;padding:11px 18px;">
                            <div style="width:34px;height:34px;border-radius:8px;background:#229ed9;display:flex;align-items:center;justify-content:center;margin-right:13px;flex-shrink:0;box-shadow:0 2px 6px rgba(34,158,217,0.35);">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                            </div>
                            <div style="flex:1;">
                                <div style="font-size:11px;color:#888;margin-bottom:1px;">Telegram</div>
                                <div style="font-size:14px;color:#1a1a1a;font-weight:500;">@rahul_telegram</div>
                            </div>
                            <a href="https://t.me/rahul_telegram" target="_blank" style="font-size:12px;color:#229ed9;text-decoration:none;font-weight:600;background:rgba(34,158,217,0.12);padding:4px 10px;border-radius:6px;">Message</a>
                        </div>

                    </div>

                    <!-- Footer hint -->
                    <div style="padding:10px 18px 16px;text-align:center;border-top:1px solid rgba(0,0,0,0.06);">
                        <span style="font-size:11px;color:#bbb;">Press ESC to close</span>
                    </div>
                </div>
            `;

            document.body.appendChild(win);

            function handleEsc(e) {
                if(e.key === 'Escape' && document.getElementById('mac-contact-card')) {
                    closeMacContactCard();
                    document.removeEventListener('keydown', handleEsc);
                }
            }
            document.addEventListener('keydown', handleEsc);
            win._escHandler = handleEsc;
        }

        function closeMacContactCard() {
            const win = document.getElementById('mac-contact-card');
            if(!win) return;
            document.removeEventListener('keydown', win._escHandler);
            const inner = document.getElementById('mac-contact-window');
            if(inner) {
                inner.style.transition = 'transform 0.16s ease-in,opacity 0.16s ease-in';
                inner.style.transform = 'scale(0.88) translateY(8px)';
                inner.style.opacity = '0';
            }
            setTimeout(() => { win.remove(); document.body.style.overflow = 'auto'; }, 170);
        }

        // ── macOS Mail Compose Window ────────────────────────────────────────────
        function openMacMailCompose() {
            if(document.getElementById('mac-mail-compose')) return;
            document.body.style.overflow = 'hidden';

            const win = document.createElement('div');
            win.id = 'mac-mail-compose';
            win.style.cssText = `
                position:fixed;inset:0;z-index:9000;display:flex;align-items:center;justify-content:center;
                background:rgba(0,0,0,0.45);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);
            `;

            win.innerHTML = `
                <div id="mac-mail-window" style="
                    font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Helvetica Neue',sans-serif;
                    width:min(620px,95vw);
                    background:rgba(242,242,247,0.97);
                    backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
                    border-radius:12px;
                    box-shadow:0 30px 90px rgba(0,0,0,0.5),0 0 0 0.5px rgba(0,0,0,0.2);
                    overflow:hidden;
                    animation:macWinPop 0.2s cubic-bezier(0.34,1.46,0.64,1);
                    display:flex;flex-direction:column;
                ">
                <style>
                    @keyframes macWinPop{from{transform:scale(0.86) translateY(10px);opacity:0}to{transform:scale(1) translateY(0);opacity:1}}
                    #mac-mail-window input,#mac-mail-window .mac-field{outline:none;border:none;background:transparent;font-family:inherit;}
                    #mac-mail-window input::placeholder{color:#b0b0b8;}
                    .mac-field-row{display:flex;align-items:center;padding:7px 16px;border-bottom:1px solid rgba(0,0,0,0.08);}
                    .mac-field-label{font-size:12px;color:#888;width:52px;flex-shrink:0;font-weight:500;}
                    .mac-field-value{font-size:13px;color:#1a1a1a;flex:1;}
                    .mac-field-locked{font-size:13px;color:#3a3a3a;flex:1;font-weight:500;}
                    .fmt-btn{
                        background:none;border:none;cursor:pointer;padding:4px 7px;border-radius:5px;
                        font-size:13px;color:#444;transition:background 0.12s,color 0.12s;line-height:1;
                    }
                    .fmt-btn:hover{background:rgba(0,0,0,0.08);color:#000;}
                    .fmt-btn.active{background:rgba(0,122,255,0.12);color:#007aff;}
                    #mac-body-editor{
                        min-height:160px;max-height:260px;overflow-y:auto;
                        padding:12px 16px;font-size:14px;line-height:1.6;color:#1a1a1a;
                        outline:none;
                    }
                    #mac-body-editor:empty:before{content:attr(data-placeholder);color:#b0b0b8;pointer-events:none;}
                    #mac-send-btn{
                        background:linear-gradient(180deg,#fecc00 0%,#f5b800 100%);
                        border:none;border-radius:7px;
                        color:#1a1000;font-size:13px;font-weight:700;
                        padding:7px 20px;cursor:pointer;
                        box-shadow:0 1px 4px rgba(0,0,0,0.18),inset 0 1px 0 rgba(255,255,255,0.45);
                        display:flex;align-items:center;gap:7px;
                        transition:filter 0.12s,transform 0.1s;
                        font-family:inherit;
                    }
                    #mac-send-btn:hover{filter:brightness(1.06);transform:translateY(-1px);}
                    #mac-send-btn:active{transform:scale(0.97);}
                    #mac-send-btn:disabled{opacity:0.5;cursor:not-allowed;transform:none;}
                    .mac-toolbar-sep{width:1px;height:18px;background:rgba(0,0,0,0.12);margin:0 2px;}
                </style>

                <!-- Title bar -->
                <div style="background:linear-gradient(180deg,#e4e4e4 0%,#d6d6d6 100%);border-bottom:1px solid #bbb;padding:11px 14px 10px;display:flex;align-items:center;position:relative;flex-shrink:0;">
                    <!-- Traffic lights -->
                    <div style="display:flex;gap:8px;z-index:1;">
                        <button onclick="closeMacMailCompose()" style="width:13px;height:13px;border-radius:50%;background:#ff5f57;border:0.5px solid #e0443e;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:7px;color:transparent;transition:color 0.1s;flex-shrink:0;" onmouseover="this.style.color='#7a0000'" onmouseout="this.style.color='transparent'">✕</button>
                        <div style="width:13px;height:13px;border-radius:50%;background:#febc2e;border:0.5px solid #d9a325;"></div>
                        <div style="width:13px;height:13px;border-radius:50%;background:#28c840;border:0.5px solid #1aab2e;"></div>
                    </div>
                    <!-- Title -->
                    <div style="position:absolute;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:6px;">
                        <span style="font-size:13px;font-weight:600;color:#2a2a2a;letter-spacing:-0.15px;">New Message</span>
                    </div>
                </div>

                <!-- Header fields -->
                <div style="background:#f7f7f7;border-bottom:1px solid rgba(0,0,0,0.1);">
                    <div class="mac-field-row">
                        <span class="mac-field-label">To</span>
                        <span class="mac-field-locked">Rahul Pal &lt;mail.rahulpal@gmail.com&gt;</span>
                        <span style="font-size:11px;background:rgba(0,122,255,0.1);color:#007aff;border-radius:4px;padding:2px 6px;margin-left:8px;font-weight:500;">rahulpal</span>
                    </div>
                    <div class="mac-field-row">
                        <span class="mac-field-label">From</span>
                        <input id="smtp-sender-input" type="email" class="mac-field-value" placeholder="your@email.com" required style="flex:1;font-family:inherit;">
                    </div>
                    <div class="mac-field-row">
                        <span class="mac-field-label">Subject</span>
                        <input id="smtp-subject-input" type="text" class="mac-field-value" value="Let's Collaborate" required style="flex:1;font-family:inherit;">
                    </div>
                </div>

                <!-- Formatting toolbar -->
                <div style="background:#f0f0f0;border-bottom:1px solid rgba(0,0,0,0.08);padding:5px 10px;display:flex;align-items:center;gap:2px;flex-wrap:wrap;">
                    <button class="fmt-btn" onclick="macFmt('bold')" title="Bold" id="fmt-bold"><b>B</b></button>
                    <button class="fmt-btn" onclick="macFmt('italic')" title="Italic" id="fmt-italic"><i>I</i></button>
                    <button class="fmt-btn" onclick="macFmt('underline')" title="Underline" id="fmt-underline"><u>U</u></button>
                    <button class="fmt-btn" onclick="macFmt('strikeThrough')" title="Strikethrough" id="fmt-strike" style="text-decoration:line-through;">S</button>
                    <div class="mac-toolbar-sep"></div>
                    <button class="fmt-btn" onclick="macFmt('justifyLeft')" title="Align left" style="font-size:12px;">&#8676;</button>
                    <button class="fmt-btn" onclick="macFmt('justifyCenter')" title="Center" style="font-size:12px;">&#8596;</button>
                    <button class="fmt-btn" onclick="macFmt('justifyRight')" title="Align right" style="font-size:12px;">&#8677;</button>
                    <div class="mac-toolbar-sep"></div>
                    <button class="fmt-btn" onclick="macFmt('insertUnorderedList')" title="Bullet list" style="font-size:12px;">&#8226;&#8801;</button>
                    <button class="fmt-btn" onclick="macFmt('insertOrderedList')" title="Numbered list" style="font-size:12px;">1&#8801;</button>
                    <div class="mac-toolbar-sep"></div>
                    <select onchange="macFmtSize(this)" style="font-size:11px;border:none;background:transparent;color:#444;cursor:pointer;outline:none;border-radius:4px;padding:2px 3px;" title="Font size">
                        <option value="2">Small</option>
                        <option value="3" selected>Normal</option>
                        <option value="4">Large</option>
                        <option value="5">Larger</option>
                    </select>
                    <div class="mac-toolbar-sep"></div>
                    <button class="fmt-btn" onclick="macFmt('removeFormat')" title="Clear formatting" style="font-size:11px;letter-spacing:-0.5px;">Aa✕</button>
                </div>

                <!-- Editable body -->
                <div id="mac-body-editor" contenteditable="true" data-placeholder="Write your message here…" spellcheck="true"></div>

                <!-- Footer -->
                <div style="background:#f0f0f0;border-top:1px solid rgba(0,0,0,0.08);padding:10px 14px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0;">
                    <span id="smtp-status-log" style="font-size:11px;color:#999;font-style:italic;">Ready to send.</span>
                    <button id="mac-send-btn" onclick="dispatchClientEmailStream(null)">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                        Send E-Mail
                    </button>
                </div>
                </div>
            `;

            document.body.appendChild(win);

            // ESC closes compose
            function handleMailEsc(e) {
                if(e.key === 'Escape' && document.getElementById('mac-mail-compose')) {
                    closeMacMailCompose();
                    document.removeEventListener('keydown', handleMailEsc);
                }
            }
            document.addEventListener('keydown', handleMailEsc);
            win._escHandler = handleMailEsc;

            setTimeout(() => document.getElementById('smtp-sender-input')?.focus(), 100);
        }

        function closeMacMailCompose() {
            const win = document.getElementById('mac-mail-compose');
            if(!win) return;
            document.removeEventListener('keydown', win._escHandler);
            const inner = document.getElementById('mac-mail-window');
            if(inner) {
                inner.style.transition = 'transform 0.16s ease-in,opacity 0.16s ease-in';
                inner.style.transform = 'scale(0.88) translateY(8px)';
                inner.style.opacity = '0';
            }
            setTimeout(() => { win.remove(); document.body.style.overflow = 'auto'; }, 170);
        }

        function macFmt(cmd) {
            document.getElementById('mac-body-editor').focus();
            document.execCommand(cmd, false, null);
            // Toggle active state on format buttons
            const map = {bold:'fmt-bold',italic:'fmt-italic',underline:'fmt-underline',strikeThrough:'fmt-strike'};
            if(map[cmd]) {
                const btn = document.getElementById(map[cmd]);
                if(btn) btn.classList.toggle('active', document.queryCommandState(cmd));
            }
        }
        function macFmtSize(sel) {
            document.getElementById('mac-body-editor').focus();
            document.execCommand('fontSize', false, sel.value);
        }

        function openTerminalModal(subsystemId) {
            const modal = document.getElementById('terminal-modal');
            const title = document.getElementById('modal-terminal-title');
            const body = document.getElementById('modal-terminal-body');
            const timestamp = new Date().toISOString().replace('T', ' ').slice(0, 19);

            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';

            if(subsystemId === 'phone') {
                // Open macOS contact card instead of terminal
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
                openMacContactCard();
                return;
            } else if(subsystemId === 'email') {
                // Don't use the terminal modal for email — open the macOS compose window
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
                openMacMailCompose();
                return;
            } else if(subsystemId === 'dispatch') {
                title.innerHTML = 'rahul_pal@software_dev:~/order_dispatch_telemetry.log';
                body.innerHTML = `<div class="whitespace-pre-wrap"><span class="text-emerald-400">[${timestamp}]</span> <span class="text-emerald-400">INCOMING METRIC REGISTRATION:</span><br>` +
                    `--------------------------------------------------------------------------------<br>` +
                    `<span class="text-yellow-400">[API_GATEWAY]</span> Trace ID: <span class="text-white font-bold">req_fa89_002a</span> | Route Context: <span class="text-cyan-400">POST /api/v1/orders/dispatch-pipeline</span><br>` +
                    `<span class="text-yellow-400">[SECURITY]</span> Authorization checked: JWT cryptographic bearer claims verified. Scope: [operator:write]<br>` +
                    `<span class="text-yellow-400">[MIDDLEWARE]</span> Applying Token Bucket Throttling logic. Cluster rate capacity: 100/100 safe.<br>` +
                    `<span class="text-yellow-400">[ORM_ENGINE]</span> Initializing relational mapper session tracking allocations.<br>` +
                    `<span class="text-yellow-400">[PERFORMANCE]</span> Executing transaction routines with optimized code mapping -> <span class="underline font-bold text-white">40% speed boost active</span>.<br>` +
                    `<span class="text-yellow-400">[DB_CONNECTION]</span> Context wrapper successfully resolved pool locks. Response state: <span class="text-emerald-400 font-bold">HTTP 201 CREATED</span> (0.42ms)</div>`;
            } else if(subsystemId === 'inventory') {
                title.innerHTML = 'rahul_pal@software_dev:~/inventory_concurrency_monitor.sh';
                body.innerHTML = `<div class="whitespace-pre-wrap"><span class="text-emerald-400">[${timestamp}]</span> <span class="text-emerald-400">CAPTURING INSTANCE STATE VECTORS:</span><br>` +
                    `--------------------------------------------------------------------------------<br>` +
                    `<span class="text-yellow-400">[LOG_MONITOR]</span> Spawning continuous analytics listener across transactional threads.<br>` +
                    `<span class="text-yellow-400">[MUTEX_LOCK_POOL]</span> Allocating secure row locks. Simultaneous connection workers: 154 metrics streaming cleanly.<br>` +
                    `<span class="text-yellow-400">[AUTHENTICATION]</span> Validating token parameters against cryptography encryption routines.<br>` +
                    `<span class="text-yellow-400">[LOGIC_CHECK]</span> Reorder parameters conditions evaluated. Current inventory footprint: SAFE_LIMITS.<br>` +
                    `<span class="text-yellow-400">[INTEGRITY]</span> Variance mitigation successfully complete. Anomaly track records: <span class="text-white font-bold">0.00%</span> (Error rates dropped by 50%).<br>` +
                    `<span class="text-yellow-400">[POOL_RELEASE]</span> Process structural execution normal. Returning connection thread arrays to core backend pool logs.</div>`;
            } else if(subsystemId === 'pipeline') {
                title.innerHTML = 'rahul_pal@software_dev:~/pandas_data_ingestion_trace.py';
                body.innerHTML = `<div class="whitespace-pre-wrap"><span class="text-emerald-400">[${timestamp}]</span> <span class="text-emerald-400">PARSING SYSTEM VECTOR TRANSFORMATIONS:</span><br>` +
                    `--------------------------------------------------------------------------------<br>` +
                    `<span class="text-yellow-400">[IO_STREAM]</span> Established secure handshake connections via Google Sheets cloud spreadsheet APIs.<br>` +
                    `<span class="text-yellow-400">[PANDAS]</span> Hydrating raw JSON cell elements data blocks into dataframes matrix structures.<br>` +
                    `<span class="text-yellow-400">[NUMPY]</span> Triggering vector math alignment operations. Data type sanitation loops active.<br>` +
                    `<span class="text-yellow-400">[DATA_STREAM_ETL]</span> Initiating multi-row insert sync on relational target database instances.<br>` +
                    `<span class="text-yellow-400">[DB_METRICS]</span> Transaction finalized without error collisions. Row data degradation index: <span class="text-white font-bold">00.00%</span>.<br>` +
                    `<span class="text-yellow-400">[INTEGRATION]</span> Real-time Power BI dashboard anchors optimized. Reporting node state: <span class="text-white font-bold">AUDIT_READY</span>.</div>`;
            }
        }

        function closeTerminalModal() {
            document.getElementById('terminal-modal').classList.add('hidden');
            document.body.style.overflow = 'auto';
        }

        window.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' || event.keyCode === 27) {
                closeTerminalModal();
            }
        });

        let rawStateArray = [];
        const canvasContainer = document.getElementById('sorting-array-canvas');
        const metricsBoard = document.getElementById('sorting-metrics-board');

        function createNewStateArray() {
            canvasContainer.innerHTML = '';
            rawStateArray = [];
            for (let i = 0; i < 45; i++) {
                let heightValue = Math.floor(Math.random() * 82) + 10;
                rawStateArray.push(heightValue);
                
                const elementBar = document.createElement('div');
                elementBar.style.height = heightValue + '%';
                elementBar.className = 'bg-blue-500 w-full rounded-t-sm transition-all duration-300 shadow-[0_0_8px_rgba(59,130,246,0.2)]';
                elementBar.id = 'bar-node-' + i;
                canvasContainer.appendChild(elementBar);
            }
            metricsBoard.innerHTML = 'Time: <span class="text-blue-600 font-bold">Ready</span> | Swaps: <span class="text-blue-600 font-bold">0</span>';
        }

        async function executeQuickSortEngine() {
            let structuralSwaps = 0;
            let startPerformanceTimestamp = performance.now();
            
            async function internalQuickSort(arr, low, high) {
                if (low >= high) return;
                let partitionIdx = await executePartition(arr, low, high);
                await Promise.all([
                    internalQuickSort(arr, low, partitionIdx - 1),
                    internalQuickSort(arr, partitionIdx + 1, high)
                ]);
            }

            async function executePartition(arr, low, high) {
                let currentPivot = arr[high];
                let trackingIdx = low;
                
                const targetPivotBar = document.getElementById('bar-node-' + high);
                if(targetPivotBar) {
                    targetPivotBar.classList.remove('bg-blue-500');
                    targetPivotBar.classList.add('bg-red-500');
                }
                
                for (let i = low; i < high; i++) {
                    if (arr[i] < currentPivot) {
                        await triggerBarSwapAnimation(arr, i, trackingIdx);
                        trackingIdx++;
                    }
                }
                await triggerBarSwapAnimation(arr, trackingIdx, high);
                
                const clearedPivotBar = document.getElementById('bar-node-' + high);
                if(clearedPivotBar) {
                    clearedPivotBar.classList.remove('bg-red-500');
                    clearedPivotBar.classList.add('bg-blue-500');
                }
                
                return trackingIdx;
            }

            async function triggerBarSwapAnimation(arr, indexA, indexB) {
                await new Promise(resolve => setTimeout(resolve, 35));
                let allocationHold = arr[indexA];
                arr[indexA] = arr[indexB];
                arr[indexB] = allocationHold;
                
                const renderedBarA = document.getElementById('bar-node-' + indexA);
                const renderedBarB = document.getElementById('bar-node-' + indexB);
                
                if(renderedBarA && renderedBarB) {
                    renderedBarA.style.height = arr[indexA] + '%';
                    renderedBarB.style.height = arr[indexB] + '%';
                    
                    renderedBarA.classList.remove('bg-blue-500');
                    renderedBarA.classList.add('bg-yellow-400');
                    renderedBarB.classList.remove('bg-blue-500');
                    renderedBarB.classList.add('bg-yellow-400');
                    
                    setTimeout(() => {
                        renderedBarA.classList.remove('bg-yellow-400');
                        renderedBarA.classList.add('bg-blue-500');
                        renderedBarB.classList.remove('bg-yellow-400');
                        renderedBarB.classList.add('bg-blue-500');
                    }, 30);
                }
                structuralSwaps++;
                let deltaTimeline = (performance.now() - startPerformanceTimestamp).toFixed(2);
                metricsBoard.innerHTML = 'Time: <span class="text-blue-600 font-bold">' + deltaTimeline + 'ms</span> | Swaps: <span class="text-blue-600 font-bold">' + structuralSwaps + '</span>';
            }

            await internalQuickSort(rawStateArray, 0, rawStateArray.length - 1);
            
            for (let i = 0; i < rawStateArray.length; i++) {
                const targetBar = document.getElementById('bar-node-' + i);
                if(targetBar) {
                    setTimeout(() => {
                        targetBar.classList.replace('bg-blue-500', 'bg-emerald-400');
                        setTimeout(() => {
                            targetBar.classList.replace('bg-emerald-400', 'bg-blue-500');
                        }, 150);
                    }, i * 15);
                }
            }
        }

        createNewStateArray();
    </script>
</body>
</html>
"""

def generate_build():
    print("[*] Compiling zero-config fail-safe execution routing...")
    with open("index.html", "w", encoding="utf-8") as file_out:
        file_out.write(HTML_TEMPLATE)
    print("[✓] Build successful. Connection handles are permanently synchronized.")

if __name__ == "__main__":
    generate_build()