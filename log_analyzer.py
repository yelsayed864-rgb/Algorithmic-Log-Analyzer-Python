from collections import defaultdict

def analyze_log(file_path):
    level_counts = defaultdict(int)
    ip_counts = defaultdict(int)
    messages = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) != 3:
                    continue

                ip, level, message = parts
                level_counts[level] += 1
                ip_counts[ip] += 1
                messages.append(message)

        print("\n===== LOG ANALYSIS REPORT =====\n")

        print("Message Type Counts:")
        for level, count in level_counts.items():
            print(f"{level}: {count}")

        print("\nIP Address Activity:")
        for ip, count in ip_counts.items():
            print(f"{ip}: {count} entries")

        print("\nMost Frequent IP:")
        most_active_ip = max(ip_counts, key=ip_counts.get)
        print(f"{most_active_ip} with {ip_counts[most_active_ip]} entries")

        print("\nUnique Messages Found:")
        unique_messages = set(messages)
        for msg in unique_messages:
            print(f"- {msg}")

    except FileNotFoundError:
        print("Error: Log file not found.")


if __name__ == "__main__":
    analyze_log("sample_log.txt")
