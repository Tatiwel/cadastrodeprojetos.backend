import subprocess
import sys
import webbrowser

scripts = {
    "run": "uvicorn app.main:app --reload",
    "test-projects": "pytest -v tests/test_projects.py",
    "docs": "http://127.0.0.1:8000/docs"
}

def main():
    if len(sys.argv) < 2:
        print("\n📜 Uso: python run.py <script>")
        print("📂 Scripts disponíveis:")
        for name in scripts:
            print(f" - {name}")
        return

    script_name = sys.argv[1]
    if script_name not in scripts:
        print(f"\n❌ Script '{script_name}' não encontrado.\n")
        return

    command = scripts[script_name]

    if command.startswith("http"):
        print(f"🌐 Abrindo no navegador: {command}")
        webbrowser.open(command)
    else:
        print(f"🚀 Executando: {command}")
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
