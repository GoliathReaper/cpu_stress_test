import multiprocessing
import time

def cpu_workload():
    while True:
        pass

def cpu_stress_test(duration):
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_workload)
        processes.append(p)
        p.start()

    time.sleep(duration)

    for p in processes:
        p.terminate()

if __name__ == "__main__":
    test_duration = 10  # duration in seconds
    print(f"Starting CPU stress test for {test_duration} seconds...")
    cpu_stress_test(test_duration)
    print("CPU stress test completed.")
