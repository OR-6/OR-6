from datetime import datetime
import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/FiraCodeNerdFontMono-Bold.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def gen_custom_prompt(t, row, user="or6", host="core", symbol=">>"):
    """Custom prompt with fancy ASCII-safe design"""
    # Fancy box drawing characters that are Latin-1 safe
    prompt = f"\x1b[96m[\x1b[95m{user}\x1b[96m@\x1b[93m{host}\x1b[96m]\x1b[0m \x1b[92m{symbol}\x1b[0m "
    t.gen_text(prompt, row)


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    
    # BIOS Screen - More realistic
    t.gen_text("CoreOS UEFI BIOS v2.5.1247", 1)
    t.gen_text(f"Copyright (C) 2015-{year_now}, \x1b[31mOR-6 Technologies\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile System BIOS - Build 2025.01.14\x1b[0m", 4)
    t.gen_text("Quantum-Core Processor @ 3.6GHz | 8 Cores", 6)
    t.gen_text(
        "Press \x1b[94mF2\x1b[0m for Setup, \x1b[94mF12\x1b[0m for Boot Menu, \x1b[94mDEL\x1b[0m for Advanced",
        t.num_rows,
    )
    
    # Memory Test with more realistic progression
    for i in range(0, 65653, 7168):
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Testing RAM: {i}KB", 7, count=2, contin=True)
        else:
            t.gen_text(f"Testing RAM: {i}KB", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB \x1b[92mPASSED\x1b[0m", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    # Enhanced Boot Sequence - Linux-style with more steps
    t.clear_frame()
    t.gen_text("\x1b[96m[    0.000000]\x1b[0m Initializing kernel", 1, count=3)
    t.gen_text("\x1b[96m[    0.124751]\x1b[0m CPU: Quantum-Core detected", 2, count=2)
    t.gen_text("\x1b[96m[    0.245891]\x1b[0m Memory: 64KB available", 3, count=2)
    
    boot_sequence = [
        "[    0.458234] PCI: Probing PCI hardware",
        "[    0.672145] ACPI: Interpreter enabled",
        "[    0.891562] ACPI: Power Button detected",
        "[    1.134782] USB: Host controller initialized",
        "[    1.367294] SCSI: Scanning for devices",
        "[    1.589431] EXT4-fs: Mounted root filesystem",
        "[    1.823674] systemd[1]: Starting system services",
        "[    2.045821] systemd[1]: Reached target Network",
        "[    2.267493] systemd[1]: Reached target Multi-User",
        "[    2.534628] systemd[1]: Startup finished",
    ]
    
    row = 4
    for line in boot_sequence:
        t.gen_text(f"\x1b[96m{line}\x1b[0m", row, count=1)
        row += 1
        if row >= t.num_rows - 1:
            break
    
    t.gen_text("", row, count=5)
    
    # OS Logo Animation
    t.gen_text("\x1b[96m", 1, count=0, contin=True)
    t.set_font(FONT_FILE_LOGO, 66)
    os_logo_text = "CORE OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    # Login Screen
    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[95mCore OS v2.1.0 LTS (tty1)\x1b[0m", 1, count=5)
    t.gen_text("", 2, count=3)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("OR-6", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"\x1b[92mAuthentication successful\x1b[0m", 6, count=5)
    t.gen_text(f"Last login: {time_now} on tty1", 7, count=5)
    t.gen_text("", 8, count=3)

    # Shell prompt with custom branding
    gen_custom_prompt(t, 9)
    prompt_col = t.curr_col
    t.clone_frame(5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 9, contin=True)
    t.delete_row(9, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 9, count=3, contin=True)

    # Fetch GitHub Stats
    ignore_repos = ["archiso-zfs", "archiso-zfs-archive"]
    git_user_details = gifos.utils.fetch_github_stats("OR-6", ignore_repos)
    user_age = gifos.utils.calc_age(18, 8, 2008)
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    
    # ASCII-only separators to avoid encoding issues
    user_details_lines = f"""
    \x1b[30;101m OR-6@GitHub \x1b[0m
    ================
    \x1b[96mOS:     \x1b[93mWindows 11, Android 14\x1b[0m
    \x1b[96mHost:   \x1b[93mDelhi Public School\x1b[94m #DPS\x1b[0m
    \x1b[96mKernel: \x1b[93mComputer Science\x1b[0m
    \x1b[96mUptime: \x1b[93m{user_age.years}y {user_age.months}m {user_age.days}d\x1b[0m
    \x1b[96mIDE:    \x1b[93mVSCode + Neovim\x1b[0m
    
    \x1b[30;102m Contact \x1b[0m
    ================
    \x1b[96mDiscord:   \x1b[93m_or1_\x1b[0m
    \x1b[96mInstagram: \x1b[93mkaunnumi\x1b[0m
    \x1b[96mEmail:     \x1b[93mornor6@gmail.com\x1b[0m
    
    \x1b[30;104m GitHub Stats \x1b[0m
    ================
    \x1b[96mRating:        \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mStars Earned:  \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mCommits ({int(year_now) - 1}):  \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs:     \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR:     \x1b[93m{git_user_details.pull_requests_merge_percentage}%\x1b[0m
    \x1b[96mContributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
    """
    
    gen_custom_prompt(t, 1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mcorefetc", 2, contin=True)
    t.delete_row(2, prompt_col)
    t.gen_text("\x1b[92mcorefetch\x1b[0m", 2, contin=True)
    t.gen_typing_text(" --user OR-6 --style matrix", 2, contin=True)

    # Mona ASCII Art
    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    # Display User Details
    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    
    # FIX: Create the row first before using gen_typing_text with contin=True
    current_row = t.curr_row
    gen_custom_prompt(t, current_row)
    
    # Now use gen_typing_text on the next row (initialize it first)
    t.gen_text("", current_row + 1)  # Initialize the row
    t.gen_typing_text(
        "\x1b[92m# Thanks for visiting! Stay curious, keep coding.",
        current_row + 1,
        contin=True,
    )
    
    # Matrix-style loading bar animation
    t.gen_text("", t.curr_row + 2, count=3)
    loading_bar = "\x1b[96m[" + "=" * 30 + "] \x1b[92m100%\x1b[0m"
    t.gen_text(loading_bar, t.curr_row + 2, count=5)
    
    # Easter egg (flashes for 1 frame)
    t.gen_text(
        "\x1b[90m// powered by late-night code sessions and infinite coffee\x1b[0m",
        t.num_rows - 1,
        count=1
    )
    t.delete_row(t.num_rows - 1)
    
    t.gen_text("", t.curr_row, count=120, contin=True)

    # Generate Output
    t.gen_gif()
    
    readme_file_content = rf"""<div align="center">

# 🚀 Welcome to Core OS

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="Core OS Terminal" src="output.gif">
</picture>

---

<sub>Built with CoreOS Technology • OR-6 © {year_now}</sub>

</div>"""
    
    with open("README.md", "w") as f:
        f.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()