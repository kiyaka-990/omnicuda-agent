# OmniCUDA-Agent ⚡
> Enterprise GPU Kernel Optimizer & Real-Time Hardware Telemetry Profiler

OmniCUDA-Agent is an AI agent and hardware profiling platform designed to analyze C++/CUDA kernel ASTs, detect memory alignment bottlenecks, resolve warp divergence, and stream live NVML GPU telemetry at 60Hz.

Built specifically for NVIDIA Hopper (`sm_90`) and Ampere architectures, OmniCUDA-Agent bridges high-level AI code refactoring with low-level GPU hardware telemetry.

---

## 🚀 Core Features

- **⚡ AST-Driven CUDA Refactoring:** Analyzes CUDA source code to detect missing `__syncthreads()` barriers, modulo thread indexing, and memory allocation leaks.
- **📊 60Hz NVML Hardware Telemetry:** Streams VRAM saturation, GPU compute utilization, power draw (Watts), and thermal margins over WebSockets via `pynvml`.
- **🧩 Warp 0 Memory Alignment Matrix:** Interactive 32-thread visualization showing coalesced memory access, warp divergence, and bank conflicts.
- **📈 Side-by-Side Throughput Benchmarking:** Evaluates performance gains across kernel latency (ms), compute throughput (TFLOPS), and memory bandwidth (GB/s).
- **📝 Nsight-Style Audit Exporter:** Generates 1-click Markdown hardware audit reports ready for enterprise CI/CD workflows.

---

## 🏗️ System Architecture

┌────────────────────────────────────────────────────────────────────────┐
│                   Next.js 15 Enterprise Dashboard                      │
│   • Monaco Editor (C++/CUDA Highlighting)                              │
│   • Recharts 60Hz WebSocket Telemetry Stream                           │
│   • Interactive Warp Memory Access Matrix                              │
└───────────────────────────────────┬────────────────────────────────────┘
│ REST API / WebSockets
▼
┌────────────────────────────────────────────────────────────────────────┐
│                     FastAPI Python Runtime Engine                      │
│   • CUDA AST Static Analyzer & Bottleneck Detector                     │
│   • NVML Hardware Telemetry Profiler (pynvml Driver Layer)             │
│   • Side-by-Side Latency & Throughput Benchmark Evaluator              │
└────────────────────────────────────────────────────────────────────────┘
---

## 📂 Repository Structure

```text
omnicuda-agent/
├── backend/
│   ├── main.py              # FastAPI server, endpoints, & WebSocket stream
│   ├── telemetry.py         # NVML GPU profiler & simulation fallback
│   └── requirements.txt     # Python backend dependencies
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js App Router (page.tsx, layout.tsx)
│   │   └── components/      # Client Dashboard component
│   ├── package.json         # Frontend dependencies
│   └── next.config.ts       # Next.js build configuration
├── .gitignore
└── README.md
🛠️ Tech StackLayerTechnologyFrontendNext.js 15, React 19, Tailwind CSS v4, Monaco Editor, Recharts, Lucide IconsBackendFastAPI (Python 3.11), Uvicorn, WebSockets, PydanticHardware TelemetryNVIDIA NVML (pynvml / nvidia-ml-py), Target Arch: sm_90 (Hopper)⚡ Quick Start (Local Setup)PrerequisitesPython 3.10+Node.js 18+ & npm1. Launch Backend ServerPowerShellcd backend
python -m venv venv

# Windows PowerShell Activation
.\venv\Scripts\Activate.ps1

# Install Dependencies
pip install -r requirements.txt

# Start FastAPI Engine
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
2. Launch Frontend ApplicationOpen a new terminal window:PowerShellcd frontend
npm install
npm run dev
Visit http://localhost:3000 in your browser.📡 API EndpointsPOST /api/v1/optimize-cudaSubmits a CUDA source string for AST memory analysis, refactoring, and throughput benchmarking.Sample Request:JSON{
  "code_payload": "__global__ void naive_kernel(float* input, float* output) { ... }",
  "target_architecture": "sm_90",
  "optimization_goal": "coalesced_memory_and_shared_mem"
}
WS /ws/telemetryOpens a WebSocket connection streaming live NVML telemetry data (gpu_utilization_pct, vram_used_gb, power_draw_watts, temperature_c).📜 LicenseMIT License. Built for the Nebius x NVIDIA Global AI Hackathon.