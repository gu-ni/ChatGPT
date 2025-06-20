INSTRUCTION_LCB = """Please transform the coding problem into a narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.**
- Build the story in **any genre or setting**—such as fantasy, sci-fi, historical, modern, dystopian, mystery, or slice-of-life—and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- You **must present the input and output format** as part of the story's narrative.
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.

The story should be structured into **six paragraphs at most**, and follow this flow:

**Background → Rules and Problem Setting → Task Explanation → Examples and Closing**

The coding problem is as follows:

"""

INSTRUCTION_HUMANEVAL = """Please transform the coding problem into a narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints, but do so only when such variables or constraints are explicitly present in the original problem. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.**
- Build the story in **any genre or setting**—such as fantasy, sci-fi, historical, modern, dystopian, mystery, or slice-of-life—and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
-You must refer to the required function’s input and output format, as well as the example format, and incorporate them clearly into the narrative flow of the story.
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.

The story should be structured into **six paragraphs at most**, and follow this flow:

**Background → Rules and Problem Setting → Task Explanation → Examples and Closing**

The coding problem is as follows:

"""


INSTRUCTION_CODEFORCES = """Please transform the coding problem into a narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.**
- Build the story in given genre and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- You **must present the input and output format** as part of the story's narrative. If the input or output has multiple lines, your story must reflect this format accurately. Avoid vague phrases like “followed by”—instead, use clear terms like “on the next line” or “on the same line.”
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.

The story should be structured into **six paragraphs at most**, and follow this flow:

**Background → Rules and Problem Setting → Task Explanation → Examples and Closing**

Use the following genre: {GENRE}

The coding problem is as follows:

"""



genres = [
    "Slice of Life School Diary",
    "Post-Apocalyptic Survival Log",
    "Corporate Espionage Thriller",
    "Mythological Hero’s Trial",
    "Time Travel Regulation Protocols",
    "Dream Architect Simulator",
    "Urban Legend Investigator Log",
    "Courtroom Logic Drama",
    "Runestone Puzzle Trials",
    "Space Opera Colony Management",
    "Heist Planning Manual",
    "Ancient Archive Puzzlekeeper",
    "Social Network Popularity Simulator",
    "Genetic Algorithm Lab Notes",
    "Historical Battlefield Logistics",
    "Fantasy Inn Resource Ledger",
    "Mystery Puzzle in Locked Mansion",
    "Underground Hacker’s Terminal Log",
    "Political Simulation RPG",
    "Kingdom Census Ledger",
    "Collaborative Task Scheduling Center",
    "Toy Factory Automation Blueprint",
    "Haunted Library Lexicon Rules",
    "E-Sports Tournament Simulation",
    "Shipwrecked Island Survival Council",
    "Chronicles of the Shifting Labyrinth",
    "Space-Time Puzzle Labyrinth",
    "Lost Civilization Number Rituals",
    "Parallel Universe Synchronization Log",
    "Board Game Rulebook Translation",
    "Carnival Game Engineering Log",
    "Train Station Announcement System",
    "Magical Candy Factory Recipes",
    "Mechanical Puppet Theatre Scripts",
    "Floating Market Merchant Ledger",
    "Arcane Academy Examination",
    "Midnight Radio Broadcast Archive",
    "Monster Evolution Guide",
    "Witch’s Alchemy Book",
    "Abandoned Theme Park Blueprint",
    "Citywide Lantern Festival Logbook",
    "Alien Zoo Containment Manual",
    "Entertainment Event Flow Designer",
    "Tea House Operations Manager",
    "Museum Night Guard Report",
    "Postcard Routing Puzzle",
    "Retro Toy Catalog Compiler",
    "Clockmaker’s Routine Notebook",
    "Ecosystem Simulation Console",
    "Festival Parade Queue Directive"
]
