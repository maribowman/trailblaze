Demo UI to test a few things and organize a BBQ.

# Development
Run `uv run main.py` to start [NiceGUI](https://nicegui.io/) app.

# Dockerize on RaspberryPi
```sh
curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
sudo usermod -aG docker $USER
```
```sh
docker build -t marschine/trailblaze .
```

```sh
docker run -d -p 6969:6969 -v ~/docker/trailblaze:/app/data --name trailblaze marschine/trailblaze:latest
```

# Cloudflared on RaspberryPi
1. Install cloudflared
    ```bash
    wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64.deb
    sudo dpkg -i cloudflared-linux-*.deb
    ```
2. Setup and authenticate tunnel
    ```
    cloudflared tunnel login  # -> click on displayed link!
    cloudflared tunnel create <TUNNEL_NAME>
    ```
3. Configure tunnel `~/.cloudflared/config.yml` with `config.yml.template`
- Configure Cloudflare DNS
  - Chose domain and go to DNS settings
  - Add new `CNAME` record mit `SUBDOMAIN` as name and `<TUNNEL_ID>.cfargotunnel.com` as target
  - Ensure proxy status is set to "Proxied"
4. <span id="start-tunnel">Start tunnel as service</span>
    ```bash
    sudo systemctl enable cloudflared  # Activate service
    sudo systemctl start cloudflared  # Start service
    sudo systemctl status cloudflared  # Check status
    # Optional
    sudo journalctl -u cloudflared -f  # Check logs
    ```

## Troubleshooting
1. Setup cloudflared service `/etc/systemd/system/cloudflared.service` with `cloudflared.service.template`
2. Reload `systemd` demon with `sudo systemctl daemon-reload` and continue with [Start tunnel as service](#start-tunnel)