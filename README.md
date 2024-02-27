# PortScan
> TCP Port Scanner Application

## Components
**TCP Port Scanner**
- **Local Host Port Scanning**
- **LAN IP and Port Scanning**

## Features

The implemented as streamlit web application that runs on the localhost.

1. The *localhost’s IP address* and the *hostname* of the device. 
- ***Multi-threading*** used to make the finding ports on the localhost more faster.
2. The machine performs a ***ping sweep*** as well as a *SYN* and ***FIN*** scan to find the IP address of all the devices and the set of vulnerable ports located on their machines.

## Tech Stack

**Languages:** python, markdown

**LocalHost:** streamlit


## Run Locally

**Clone the project**

```bash
  git clone https://github.com/AlanJoji/PortScan.git
```

**Go to the project directory**

```bash
  cd PortScan
```

**Install dependencies**

1. For Multi-threading|processing
```bash
  pip install multiprocessing
```

2. For OS independent ping sweep
```bash
  pip install ping3
```

3. For streamlit 
```bash
  pip install streamlit
```

**Run the Program**
```bash
    streamlit run main.py
```


## Authors

- [Alan Joji](https://github.com/AlanJoji)
- [Vaibhav Abhiramacheri](https://github.com/Whybhuv)
- [Aditya A S](https://github.com/ad1tya24)



