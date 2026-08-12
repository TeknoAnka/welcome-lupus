# AeroSky ☀️🌤️☁️

Ultra Modern, Fast, and Elegant Weather Application — **Built with Rust & Tauri 2**

AeroSky is an ultra-modern desktop weather application built with Rust and Tauri 2, utilizing Open-Meteo, Nominatim, and IP Geolocation services to provide comprehensive weather forecasts.

---

## ✨ Features

- ⚡ **Powered by Rust & Tauri 2**: Lightweight footprint, fast startup, and high performance.
- 🎨 **Glassmorphism & Modern UI**: Animated canvas background, sleek glass cards, and smooth micro-interactions.
- 🌐 **Auto Language Detection**: Multi-language support with automatic detection for English (EN) and Turkish (TR).
- 📍 **Location Detection & City Search**: IP-based automatic device location detection or worldwide search via Nominatim API.
- 📊 **Detailed Weather Forecasts**:
  - Current temperature, feels-like temperature, Humidity, Wind speed, UV Index, Surface Pressure, Sunrise/Sunset times, and Precipitation Probability.
  - **Hourly Forecast**: Hour-by-hour forecast for the next 24 hours.
  - **7-Day Forecast**: Weekly weather outlook.
- 🏠 **Search History & Startup Location**: Quick-access chips for recent searches and custom default startup city setting.

---

## 🛠️ Prerequisites

- **Rust & Cargo** (`>= 1.75`)
- **Tauri v2 CLI** (`cargo install tauri-cli`)
- **System Libraries (Linux)**: `webkit2gtk`, `gtk3`, `openssl`

---

## 🚀 Building & Running

### Development Mode
```bash
cargo tauri dev
# or using Makefile
make run
```

### Production Release Build
```bash
cd src-tauri && cargo build --release
# or using Makefile
make build
```

---

## 📦 Packaging for PiSi Package Manager

AeroSky fully supports the **PiSi Linux** package manager format. To build the `.pisi` package automatically:

```bash
./build-pisi.sh
# or using Makefile
make package
```

Upon successful compilation, the `aerosky-2.0.0-1-p20-x86_64.pisi` package will be created in the root directory. To install it:

```bash
sudo pisi install aerosky-*.pisi
```

---

## 📜 License

This project is licensed under the [GPLv3 License](LICENSE).
