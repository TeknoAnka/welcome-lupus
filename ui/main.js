window.addEventListener('DOMContentLoaded', () => {
  // Tauri API'sinin yüklenip yüklenmediğini kontrol et
  const tauri = window.__TAURI__;

  if (!tauri) {
    console.error("Tauri API yüklenemedi. tauri.conf.json dosyasında withGlobalTauri: true olduğundan emin olun.");
    return;
  }

  const { invoke } = tauri.core;

  // 1. Rust Komut Çalıştırıcı Yardımcısı
  function runCmd(cmd, args = []) {
    invoke('run_command', { cmd: cmd, args: args })
      .catch(err => console.error("Komut çalıştırma hatası:", err));
  }

  function runInTerminal(commandStr) {
    invoke('run_in_terminal', { commandStr: commandStr })
      .catch(err => console.error("Terminal komut hatası:", err));
  }

  // 2. Uygulama Butonları
  document.getElementById('btn-kaptan')?.addEventListener('click', () => runCmd('kaptan'));
  document.getElementById('btn-pisim')?.addEventListener('click', () => runCmd('pisim'));
  document.getElementById('btn-graphics')?.addEventListener('click', () => runCmd('pisidi'));
  document.getElementById('btn-dns')?.addEventListener('click', () => runCmd('dns-changer'));
  document.getElementById('btn-printer')?.addEventListener('click', () => runCmd('system-config-printer'));

  document.getElementById('btn-gaming')?.addEventListener('click', () => runInTerminal('sudo pisi it lupus-gaming-packages'));
  document.getElementById('btn-waydroid')?.addEventListener('click', () => runInTerminal('sudo pisi it waydroid'));
  document.getElementById('btn-winboat')?.addEventListener('click', () => runInTerminal('sudo pisi it winboat'));

  // 3. Sosyal Medya Linkleri
  document.getElementById('btn-website')?.addEventListener('click', () => window.open('https://www.teknoanka.com', '_blank'));
  document.getElementById('btn-github')?.addEventListener('click', () => window.open('https://github.com/TeknoAnka', '_blank'));
  document.getElementById('btn-x')?.addEventListener('click', () => window.open('https://x.com/TeknoAnka', '_blank'));
  document.getElementById('btn-youtube')?.addEventListener('click', () => window.open('https://www.youtube.com/@TeknoAnkaOfficial', '_blank'));

  // 4. Otomatik Başlatma (Autostart)
  const autostartCb = document.getElementById('autostart-cb');
  if (autostartCb && tauri.plugin && tauri.plugin.autostart) {
    const { enable, disable, isEnabled } = tauri.plugin.autostart;

    isEnabled().then(enabled => {
      autostartCb.checked = enabled;
    }).catch(console.error);

    autostartCb.addEventListener('change', (e) => {
      if (e.target.checked) {
        enable().catch(console.error);
      } else {
        disable().catch(console.error);
      }
    });
  }
});