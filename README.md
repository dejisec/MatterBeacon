# MatterBeacon

An Aggressor Script and a Python script to notify you via Mattermost whenever a new beacon checks in.

## **Setup and Configuration**

1. **Set Up Mattermost Webhook**:
   - Go to your Mattermost server.
   - Navigate to **Integrations** > **Incoming Webhooks** > **Add Incoming Webhook**.
   - Copy the generated webhook URL.

2. **Edit Python Script (`alert_handler.py`)**:
   - Replace the placeholder `webhookurl` value with your Mattermost webhook URL:
     ```python
     webhookurl = "https://your-mattermost-url/hooks/your-webhook-id"
     ```

3. **Edit AggressorScript**:
   - Update the `script_path` variable in the AggressorScript with the absolute path to the `alert_handler.py` file:
     ```bash
     $script_path = "/absolute/path/to/alert_handler.py";
     ```

---

### **Usage**

1. **Load the CNA Script**:
   - Use the AggressorScript console to load the CNA file:
     ```bash
     ./agscript [C2 IP] [C2 Port] [username] [C2 password] [path to CNA file]
     ```

2. **Trigger Beacon Detection**:
   - Once the script is loaded, it will automatically listen for `beacon_initial` events.
   - When a new beacon is detected, a notification will be sent to the configured Mattermost channel.

---

### **Credits**
- [BeaconNotifier-Discord](https://github.com/ScriptIdiot/BeaconNotifier-Discord)
- [beacon_notify_discordhook](https://github.com/CodeXTF2/beacon_notify_discordhook)