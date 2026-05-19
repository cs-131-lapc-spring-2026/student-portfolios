// ============================================================
//
// Scenario:
// A monitoring service continuously receives CPU metrics
// from servers running in a cloud environment.
// ============================================================

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {

    // --------------------------------------------------------
    // Simulated incoming CPU metrics
    // --------------------------------------------------------
    vector<int> cpuMetrics = {
        35, 38, 40, 42, 44,
        43, 45, 46, 47, 92
    };

    // Queue represents a real-time monitoring stream
    queue<int> monitoringQueue;

    // --------------------------------------------------------
    // Push metrics into queue
    // --------------------------------------------------------
    for (int metric : cpuMetrics) {
        monitoringQueue.push(metric);
    }

    cout << "===== REAL-TIME MONITORING =====" << endl;

    // --------------------------------------------------------
    // Process incoming metrics one at a time
    // --------------------------------------------------------
    while (!monitoringQueue.empty()) {

        int currentCPU = monitoringQueue.front();
        monitoringQueue.pop();

        cout << "CPU Usage: " << currentCPU << "%" << endl;

        // ----------------------------------------------------
        // Threshold-based alert system
        // ----------------------------------------------------
        // Traditional infrastructure systems often use
        // static thresholds like this.
        // ----------------------------------------------------
        if (currentCPU > 80) {
            cout << "ALERT: CPU usage is critically high!"
                << endl;

            cout << "Possible scaling action triggered."
                << endl;
        }

        cout << endl;
    }

    cout << "Monitoring session complete." << endl;

    return 0;
}