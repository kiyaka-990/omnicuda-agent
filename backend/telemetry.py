import time
from importlib import import_module
from typing import Dict, Any

try:
    pynvml = import_module("pynvml")
    HAS_PYNVML = True
except ImportError:
    HAS_PYNVML = False

class NVMLGPUProfiler:
    def __init__(self):
        if HAS_PYNVML:
            try:
                pynvml.nvmlInit()
                self.device_count = pynvml.nvmlDeviceGetCount()
                self.initialized = True
            except Exception:
                self.initialized = False
        else:
            self.initialized = False

    def get_metrics(self, device_index: int = 0) -> Dict[str, Any]:
        if not self.initialized or not HAS_PYNVML or device_index >= self.device_count:
            # Fallback simulated metrics for local CPU environment testing
            return {
                "gpu_name": "NVIDIA H100 80GB PCIe (Simulated)",
                "vram_used_gb": 34.2,
                "vram_total_gb": 80.0,
                "vram_utilization_pct": 42.75,
                "gpu_utilization_pct": 88.5,
                "power_draw_watts": 285.0,
                "temperature_c": 54,
                "timestamp": time.time()
            }

        handle = pynvml.nvmlDeviceGetHandleByIndex(device_index)
        name = pynvml.nvmlDeviceGetName(handle)
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        power = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0  # mW to W
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        return {
            "gpu_name": name,
            "vram_used_gb": round(mem_info.used / (1024**3), 2),
            "vram_total_gb": round(mem_info.total / (1024**3), 2),
            "vram_utilization_pct": round((mem_info.used / mem_info.total) * 100, 2),
            "gpu_utilization_pct": utilization.gpu,
            "power_draw_watts": round(power, 1),
            "temperature_c": temp,
            "timestamp": time.time()
        }

profiler = NVMLGPUProfiler()