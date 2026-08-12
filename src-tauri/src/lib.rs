use std::process::Command;

#[tauri::command]
fn run_command(cmd: String, args: Vec<String>) -> Result<(), String> {
    Command::new(cmd)
        .args(args)
        .spawn()
        .map_err(|e| e.to_string())?;
    Ok(())
}

#[tauri::command]
fn run_in_terminal(command_str: String) -> Result<(), String> {
    Command::new("alacritty")
        .args(["--command", "sh", "-c", &command_str])
        .spawn()
        .map_err(|e| e.to_string())?;
    Ok(())
}

pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_autostart::init(
            tauri_plugin_autostart::MacosLauncher::AppleScript,
            Some(vec!["--autostart"]),
        ))
        .invoke_handler(tauri::generate_handler![run_command, run_in_terminal])
        .run(tauri::generate_context!())
        .expect("Tauri uygulaması başlatılırken hata oluştu");
}