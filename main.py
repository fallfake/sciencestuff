import curses

organelles = {
    "Nucleus": "The control center of the cell that contains the cell's DNA and regulates gene expression.",
    "Mitochondria": "The powerhouse of the cell, producing energy (ATP) through cellular respiration.",
    "Ribosome": "Responsible for synthesizing proteins by translating RNA into proteins.",
    "Rough Endoplasmic Reticulum": "Covered with ribosomes and involved in the synthesis and modification of proteins.",
    "Smooth Endoplasmic Reticulum": "Involved in the synthesis of lipids and detoxification of harmful substances.",
    "Golgi Apparatus": "Modifies, sorts, and packages proteins and lipids for transport or storage.",
    "Lysosome": "Contains digestive enzymes that break down waste materials and cellular debris.",
    "Peroxisome": "Breaks down fatty acids and detoxifies harmful chemicals.",
    "Cytoskeleton": "Provides structural support and enables cell movement.",
    "Chloroplast": "Found in plant cells, responsible for converting sunlight into energy via photosynthesis.",
    "Cell Membrane": "A semipermeable barrier that controls what enters and leaves the cell.",
    "Vacuole": "Stores nutrients, waste products, and maintains turgor pressure in plant cells.",
    "Cell Wall": "Provides structural support and protection for plant cells.",
    "Centrosome": "Organizes microtubules and plays a key role in cell division."
}

def main(stdscr):
    curses.curs_set(0)

    organelle_list = list(organelles.keys())
    current_selection = 0
    selected_items = set()

    while True:
        stdscr.clear()
        stdscr.addstr("Use arrow keys to navigate, space/enter to select, 'q' to quit.\n\n")

        for idx, organelle in enumerate(organelle_list):
            if idx == current_selection:
                stdscr.addstr(f"> {organelle}\n", curses.A_REVERSE) 
            else:
                stdscr.addstr(f"  {organelle}\n")

        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1  
        elif key == curses.KEY_DOWN and current_selection < len(organelle_list) - 1:
            current_selection += 1  
        elif key == ord(' '):
            selected_item = organelle_list[current_selection]
            selected_items.add(selected_item)
            stdscr.clear()
            stdscr.addstr(f"You selected: {selected_item}\n\n{organelles[selected_item]}\n")
            stdscr.addstr("\nPress any key to return to the menu.")
            stdscr.getch()  
        elif key == ord('\n'):
            selected_item = organelle_list[current_selection]
            selected_items.add(selected_item)
            stdscr.clear()
            stdscr.addstr(f"You selected: {selected_item}\n\n{organelles[selected_item]}\n")
            stdscr.addstr("\nPress any key to return to the menu.")
            stdscr.getch()  
        elif key == ord('q'):
            break  

        stdscr.refresh()

# Run the program with curses wrapper
curses.wrapper(main)
