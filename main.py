import curses

# Dictionary of organelles and their definitions
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

# Function to handle user input with curses
def main(stdscr):
    # Disable blinking cursor
    curses.curs_set(0)

    # Get all the organelle names in a list for easy navigation
    organelle_list = list(organelles.keys())
    current_selection = 0
    selected_items = set()

    while True:
        stdscr.clear()
        stdscr.addstr("Use arrow keys to navigate, space to select, 'q' to quit.\n\n")

        # Loop through and display organelles with highlight for the selected one
        for idx, organelle in enumerate(organelle_list):
            if idx == current_selection:
                stdscr.addstr(f"> {organelle}\n", curses.A_REVERSE)  # Highlight selected organelle
            else:
                stdscr.addstr(f"  {organelle}\n")

        # Wait for user input
        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1  # Move selection up
        elif key == curses.KEY_DOWN and current_selection < len(organelle_list) - 1:
            current_selection += 1  # Move selection down
        elif key == ord(' '):
            selected_item = organelle_list[current_selection]
            selected_items.add(selected_item)
            stdscr.clear()
            stdscr.addstr(f"You selected: {selected_item}\n\n{organelles[selected_item]}\n")
            stdscr.addstr("\nPress any key to return to the menu.")
            stdscr.getch()  # Wait for key press
        elif key == ord('q'):
            break  # Exit the program

        stdscr.refresh()

# Run the program with curses wrapper
curses.wrapper(main)
