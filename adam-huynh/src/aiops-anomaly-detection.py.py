# ============================================================
# AIOps Infrastructure Monitoring Demo
# ============================================================
# This example demonstrates:
# 1. Moving averages
# 2. Standard deviation
# 3. Z-score anomaly detection
#
# Scenario:
# We are monitoring CPU utilization from a cloud server.
# AI/AIOps systems often use statistics like these to
# detect abnormal behavior before failures occur.
# ============================================================

import statistics

# Simulated CPU utilization samples over time
cpu_usage = [
    41, 43, 44, 42, 45,
    46, 44, 43, 42, 45,
    44, 43, 90  # <- anomaly spike
]

# ============================================================
# STEP 1: Calculate Moving Average
# ============================================================
# This gives us a baseline of normal system behavior.
# ============================================================

moving_average = sum(cpu_usage[:-1]) / len(cpu_usage[:-1])

print("===== MOVING AVERAGE =====")
print(f"Baseline CPU Average: {moving_average:.2f}%")
print()

# ============================================================
# STEP 2: Calculate Standard Deviation
# ============================================================
# Standard deviation measures how spread out the data is.
# ============================================================

std_dev = statistics.stdev(cpu_usage[:-1])

print("===== STANDARD DEVIATION =====")
print(f"Normal Variation: {std_dev:.2f}")
print()

# ============================================================
# STEP 3: Calculate Z-Score
# ============================================================
# Formula:
# z = (x - mean) / standard_deviation
#
# A large z-score means the value is statistically unusual.
# ============================================================

current_value = cpu_usage[-1]

z_score = (current_value - moving_average) / std_dev

print("===== Z-SCORE ANALYSIS =====")
print(f"Current CPU Value: {current_value}%")
print(f"Z-Score: {z_score:.2f}")
print()

# ============================================================
# STEP 4: Detect Anomaly
# ============================================================
# Many AIOps systems use thresholds such as:
# z-score > 2 or z-score > 3
# ============================================================

if z_score > 2:
    print("ALERT: Anomaly Detected!")
    print("Possible infrastructure issue or traffic spike.")
else:
    print("System behavior is normal.")