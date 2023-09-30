## Network Scanner

A simple network scanner tool built using Python and Scapy. This tool can scan networks using either ICMP echo requests or TCP SYN packets.

### Features

- **ICMP Scan**: Sends ICMP echo request packets to discover hosts.
- **TCP Scan**: Sends TCP SYN packets to a specific port to discover hosts.

### Installation

1. Clone this repository:
```
git clone <repository-url>
```

2. Navigate to the directory:
```
cd <repository-name>
```

3. Install the required libraries:
```
pip install -r requirements.txt
```
(Note: The `requirements.txt` file should have `scapy` listed.)

### Usage

Run the scanner:
```
python network_scanner.py
```

Follow the on-screen prompts to provide the subnet and scanning mode.

### Caution

**Always obtain proper authorization before scanning any network. Unauthorized scanning is illegal and unethical.**

### License

This project is open-sourced under the [MIT License](LICENSE).
