from datetime import datetime
import gifos
from zoneinfo import ZoneInfo
import random

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/FiraCodeNerdFontMono-Bold.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def gen_custom_prompt(t, row, user="or6", host="core", symbol=">>"):
    """Custom prompt with fancy ASCII-safe design"""
    prompt = f"\x1b[96m[\x1b[95m{user}\x1b[96m@\x1b[93m{host}\x1b[96m]\x1b[0m \x1b[92m{symbol}\x1b[0m "
    t.gen_text(prompt, row)


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    
    # BIOS Screen
    t.gen_text("CoreOS UEFI BIOS v2.5.1247", 1)
    t.gen_text(f"Copyright (C) 2015-{year_now}, \x1b[31mOR-6 Technologies\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile System BIOS - Build 2025.01.14\x1b[0m", 4)
    t.gen_text("Quantum-Core Processor @ 3.6GHz | 8 Cores", 6)
    t.gen_text(
        "Press \x1b[94mF2\x1b[0m for Setup, \x1b[94mF12\x1b[0m for Boot Menu, \x1b[94mDEL\x1b[0m for Advanced",
        t.num_rows,
    )
    
    # Memory Test
    for i in range(0, 65653, 7168):
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Testing RAM: {i}KB", 7, count=2, contin=True)
        else:
            t.gen_text(f"Testing RAM: {i}KB", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB \x1b[92mPASSED\x1b[0m", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    # Boot Sequence
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
    
    t.gen_text("", row, count=8)
    
    # OS Logo Animation
    t.clear_frame()
    t.set_font(FONT_FILE_LOGO, 66)
    os_logo_text = "CORE OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    
    t.clone_frame(3)
    
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)
    
    t.clone_frame(10)

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
    t.gen_text("", 8, count=5)

    # Shell prompt
    gen_custom_prompt(t, 9)
    prompt_col = t.curr_col
    t.clone_frame(8)
    t.toggle_show_cursor(True)
    
    # Type "clear" slower
    t.gen_text("\x1b[91mc", 9, count=2, contin=True)
    t.gen_text("\x1b[91ml", 9, count=2, contin=True)
    t.gen_text("\x1b[91me", 9, count=2, contin=True)
    t.gen_text("\x1b[91ma", 9, count=2, contin=True)
    t.gen_text("\x1b[91mr", 9, count=2, contin=True)
    t.delete_row(9, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 9, count=5, contin=True)

    # Fetch GitHub Stats
    ignore_repos = []
    git_user_details = gifos.utils.fetch_github_stats("OR-6", ignore_repos)
    user_age = gifos.utils.calc_age(18, 8, 2008)
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    
    # Prepare user details data
    user_data = {
        "Discord": "_or1_",
        "Instagram": "kaunnumi",
        "Email": "ornor6@gmail.com",
        "Rating": git_user_details.user_rank.level,
        "Stars Earned": str(git_user_details.total_stargazers),
        "Commits": str(git_user_details.total_commits_last_year),
        "Total PRs": str(git_user_details.total_pull_requests_made),
        "Merged PR": f"{git_user_details.pull_requests_merge_percentage}%",
        "Contributions": str(git_user_details.total_repo_contributions),
    }
    
    # Pick a random field to animate filling
    animated_field = random.choice(list(user_data.keys()))
    
    # Build user details with placeholder for animated field
    user_details_lines = f"""\x1b[30;101m OR-6@GitHub \x1b[0m
================
\x1b[96mOS:     \x1b[93mWindows 11, Android 14\x1b[0m
\x1b[96mHost:   \x1b[93mDelhi Public School\x1b[94m #DPS\x1b[0m
\x1b[96mKernel: \x1b[93mComputer Science\x1b[0m
\x1b[96mUptime: \x1b[93m{user_age.years}y {user_age.months}m {user_age.days}d\x1b[0m
\x1b[96mIDE:    \x1b[93mVSCode\x1b[0m

\x1b[30;102m Contact \x1b[0m
================
\x1b[96mDiscord:   \x1b[93m{user_data['Discord'] if animated_field != 'Discord' else ''}\x1b[0m
\x1b[96mInstagram: \x1b[93m{user_data['Instagram'] if animated_field != 'Instagram' else ''}\x1b[0m
\x1b[96mEmail:     \x1b[93m{user_data['Email'] if animated_field != 'Email' else ''}\x1b[0m

\x1b[30;104m GitHub Stats \x1b[0m
================
\x1b[96mRating:        \x1b[93m{user_data['Rating'] if animated_field != 'Rating' else ''}\x1b[0m
\x1b[96mStars Earned:  \x1b[93m{user_data['Stars Earned'] if animated_field != 'Stars Earned' else ''}\x1b[0m
\x1b[96mCommits ({int(year_now) - 1}):  \x1b[93m{user_data['Commits'] if animated_field != 'Commits' else ''}\x1b[0m
\x1b[96mTotal PRs:     \x1b[93m{user_data['Total PRs'] if animated_field != 'Total PRs' else ''}\x1b[0m
\x1b[96mMerged PR:     \x1b[93m{user_data['Merged PR'] if animated_field != 'Merged PR' else ''}\x1b[0m
\x1b[96mContributions: \x1b[93m{user_data['Contributions'] if animated_field != 'Contributions' else ''}\x1b[0m
\x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m"""
    
    gen_custom_prompt(t, 1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    
    # Type "corefetch" slower
    t.gen_text("\x1b[91mc", 1, count=2, contin=True)
    t.gen_text("\x1b[91mo", 1, count=2, contin=True)
    t.gen_text("\x1b[91mr", 1, count=2, contin=True)
    t.gen_text("\x1b[91me", 1, count=2, contin=True)
    t.gen_text("\x1b[91mf", 1, count=2, contin=True)
    t.gen_text("\x1b[91me", 1, count=2, contin=True)
    t.gen_text("\x1b[91mt", 1, count=2, contin=True)
    t.gen_text("\x1b[91mc", 1, count=2, contin=True)
    t.gen_text("\x1b[91mh", 1, count=2, contin=True)
    
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mcorefetch\x1b[0m", 1, count=3, contin=True)
    t.gen_text(" --user OR-6 --format dev", 1, count=5, contin=True)

    # GitHub Mona - Clean, simple design
    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    
    # Simplified clean Mona mascot
    mona_lines = [
        "     }}     }}",
        "    }}}}   }}}}",
        "    }}}}} }}}}}",
        "   }}}}}}}}}}}}}",
        "   }}}}}}}}}}}}}}",
        "   }}}}}}}}}}}}}}",
        "  }}}}}}}}}}}}}}",
        "  }}}}}}}}}}}}}}",
        "  }}}}}}}}}}}}}}",
        "}}}}}}}}}}}}}}}}}",
        "  }}}}}}}}}}}}}}",
        " }}}}}}}}}}}}}}}}",
        "}  }}}}}}}}}}  }",
        "        }}}}}",
        "       }}}}}}}",
        "       }}}}}}}}",
        "      }}}}}}}}}}",
        "     }}}}}}}}}}}",
        "     }}}}}}}}}}}}",
        "     }} }}}}}} }}",
        "        }}}}}}}",
        "         }}} }}",
    ]
    
    # Display Mona
    for i, line in enumerate(mona_lines):
        t.gen_text("\x1b[96m" + line + "\x1b[0m", 3 + i, 2, count=1)

    # Display User Details 
    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(False)
    
    # Display text starting at row 4, column 40
    start_row = 4
    start_col = 40
    details_lines = user_details_lines.split('\n')
    
    for i, line in enumerate(details_lines):
        t.gen_text(line, start_row + i, start_col, count=1)
    
    # Calculate exact positions for animated field
    field_positions = {
        "Discord": (start_row + 10, start_col + 11),
        "Instagram": (start_row + 11, start_col + 11),
        "Email": (start_row + 12, start_col + 11),
        "Rating": (start_row + 16, start_col + 15),
        "Stars Earned": (start_row + 17, start_col + 15),
        "Commits": (start_row + 18, start_col + 17),
        "Total PRs": (start_row + 19, start_col + 15),
        "Merged PR": (start_row + 20, start_col + 15),
        "Contributions": (start_row + 21, start_col + 15),
    }
    
    # Wait before animation
    t.clone_frame(15)
    
    # Animate the random field
    if animated_field in field_positions:
        field_row, field_col = field_positions[animated_field]
        value = user_data[animated_field]
        
        # Show visible cursor movement - start from a visible position
        t.toggle_show_cursor(True)
        
        # Start cursor at beginning of text area
        start_nav_row = start_row + 8
        t.gen_text("", start_nav_row, start_col + 5, count=5)
        
        # Move cursor down slowly and visibly
        for nav_row in range(start_nav_row + 1, field_row + 1):
            t.gen_text("", nav_row, start_col + 5, count=4)
        
        # Move cursor right to the field
        t.gen_text("", field_row, field_col - 5, count=3)
        t.gen_text("", field_row, field_col, count=5)
        
        # Type each character slowly
        for char in value:
            t.gen_text(f"\x1b[93m{char}\x1b[0m", field_row, count=3, contin=True)
        
        t.toggle_show_cursor(False)
        t.clone_frame(8)
    
    # Hold display
    t.clone_frame(80)
    
    # Proper nano-style bottom bar
    t.set_font(FONT_FILE_BITMAP, 15)
    
    # Create proper nano bar spanning full width
    nano_commands = "^X Exit  ^O Save  ^R Read  ^W Where  ^K Cut  ^U Paste"
    # Make bar with inverted colors
    t.gen_text(f"\x1b[30;107m {nano_commands:<{t.num_cols-2}} \x1b[0m", t.num_rows, 1, count=30)
    
    # Show exit prompt on the line above
    t.gen_text("\x1b[93mSave modified buffer? (Y/N) \x1b[0m", t.num_rows - 1, 1, count=8)
    t.toggle_show_cursor(True)
    t.gen_text("\x1b[92mN\x1b[0m", t.num_rows - 1, count=5, contin=True)
    t.toggle_show_cursor(False)
    t.clone_frame(10)
    
    # Clear and goodbye
    t.clear_frame()
    t.gen_text("", 1, count=5)
    
    goodbye_row = (t.num_rows + 1) // 2
    t.gen_text("\x1b[96m>> Logging out...\x1b[0m", goodbye_row, count=10)
    t.gen_text("\x1b[92m>> Thanks for visiting! Keep coding and stay curious.\x1b[0m", goodbye_row + 2, count=20)
    t.gen_text("\x1b[93m>> See you soon, developer!\x1b[0m", goodbye_row + 4, count=30)
    
    t.gen_text("", 1, count=20)

    # Generate Output
    t.gen_gif()
    
    readme_file_content = rf"""<div align="center">

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