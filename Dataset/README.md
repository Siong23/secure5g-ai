# 5G Network Anomaly Dataset Processing Step

This README.md will show how to convert raw packet captures (pcapng) into machine learning–ready datasets(.csv).

---

## 🌐 Step 1: Capture Raw Traffic

Collect raw packet captures from your 5G test lab using Wireshark

Store them in:

## 🧰 Step 2: Remove GTP Layer (TraceWrangler)

Open TraceWrangler → Load your `.pcapng` file → Apply **Remove GTP-U** protocol fixup → Save as a new `.pcap`.

![TraceWrangler Remove GTP](images/tracewrangler.png)


