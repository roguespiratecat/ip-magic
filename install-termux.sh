# 

install() {
    if hash ipscan 2>/dev/null; then
        echo "[*] Angry IP Scanner Installed\n"
        ipscan -h
    else
        echo "Installing Angry IP Commandline Utility"
        apt update && sudo apt upgrade -y
        apt-get  install ./core/ipscan_3.7.6_all.deb
        apt-get -f install
    fi
}

install 