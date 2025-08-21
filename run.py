#!/usr/bin/env python3
#Developers : MexazoExecuted
#TEAM : YOUTH OF PANTURA
#Info : Script Ini Gratis Dan Jangan Di Jual !!!
#Contact : t.me/Abenkkyoy
# YAH ELAH KEK ORANG SUSAH AJA DI DECODE GOBLOK!!!

import requests,os,time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from os import system
from time import sleep

system("clear")
console = Console()



def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            console.print(f"[bold red]ERROR[/bold red] Pengguna '{username}' tidak ditemukan!")
            return None
        else:
            console.print(f"[bold red]ERROR[/bold red] Batas API terlampaui atau error lainnya.")
            return None
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]ERROR[/bold red] Error koneksi: {e}")
        return None

def format_date(date_string):
    if date_string:
        date_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        return date_obj.strftime('%d %B %Y')
    return "Tidak tersedia"

def main():
    console.print(Panel("""

[bold red]  ██████╗  ██╗ ████████╗  ██████╗ ██╗  ██╗ ███████╗  ██████╗ ██╗  ██╗
 ██╔════╝  ██║ ╚══██╔══╝ ██╔════╝ ██║  ██║ ██╔════╝ ██╔════╝ ██║ ██╔╝
 ██║  ███╗ ██║    ██║    ██║      ███████║ █████╗   ██║      █████╔╝
[bold white] ██║   ██║ ██║    ██║    ██║      ██╔══██║ ██╔══╝   ██║      ██╔═██╗
 ╚██████╔╝ ██║    ██║    ╚██████╗ ██║  ██║ ███████╗ ╚██████╗ ██║  ██╗
  ╚═════╝  ╚═╝    ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚══════╝  ╚═════╝ ╚═╝  ╚═╝

[bold cyan][+] Developers : MexazoExecuted
[+] Information Script : Mengambil Informasi Akun Github
[+] Status : Online""",width=80,border_style="bold white"))
    username = console.input("[bold white]Masukkan Username Target : ")
    if not username.strip():
        console.print("[bold red]ERROR[/bold red] Username tidak boleh kosong!")
        return
        console.print(f"\n[green]Menyelidiki pengguna GitHub:[/green] [bold yellow]{username}[/bold yellow]\n")
    
    # Dapatkan informasi pengguna
    user_info = get_user_info(username)
    if not user_info:
        return
    
    # Tampilkan informasi dasar
    basic_info = f"""
[cyan]Nama:[/cyan] {user_info.get('name', 'Tidak tersedia')}
[cyan]Username:[/cyan] {user_info.get('login', 'Tidak tersedia')}
[cyan]ID:[/cyan] {user_info.get('id', 'Tidak tersedia')}
[cyan]Bio:[/cyan] {user_info.get('bio', 'Tidak tersedia')}
[cyan]Lokasi:[/cyan] {user_info.get('location', 'Tidak tersedia')}
[cyan]Perusahaan:[/cyan] {user_info.get('company', 'Tidak tersedia')}
[cyan]Blog/Website:[/cyan] {user_info.get('blog', 'Tidak tersedia')}
[cyan]Twitter:[/cyan] {user_info.get('twitter_username', 'Tidak tersedia')}
[cyan]Email:[/cyan] {user_info.get('email', 'Tidak tersedia')}
[cyan]Dapat dipekerjakan:[/cyan] {'Ya' if user_info.get('hireable') else 'Tidak'}
[cyan]Akun dibuat:[/cyan] {format_date(user_info.get('created_at'))}
[cyan]Terakhir diperbarui:[/cyan] {format_date(user_info.get('updated_at'))}
[cyan]Profil GitHub:[/cyan] {user_info.get('html_url', 'Tidak tersedia')}
"""
    console.print(Panel(basic_info, title="[bold cyan]INFORMASI", border_style="bold white"))
    stats_info = f"""
[cyan]Repositori Publik:[/cyan] {user_info.get('public_repos', 0)}
[cyan]Gists Publik:[/cyan] {user_info.get('public_gists', 0)}
[cyan]Pengikut:[/cyan] {user_info.get('followers', 0)}
[cyan]Mengikuti:[/cyan] {user_info.get('following', 0)}
"""
    console.print(Panel(stats_info, title="[bold cyan]STATISTIK", border_style="bold white"))

if __name__ == "__main__":
    main()
