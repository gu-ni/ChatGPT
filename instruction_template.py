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

- You may use alphabetical symbols for quantity-related variables (such as n, m, k). However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.**
- Build the story in given genre and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- You **must present the input and output format** as part of the story's narrative. If there are multiple inputs, each input is provided on a separate line. If the input or output has multiple lines, your story must reflect this format accurately. Avoid vague phrases like “followed by”—instead, use clear terms like “on the next line” or “on the same line.”
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.
- Do **not** include any intermediate steps that could assist in solving the problem. You **must use only the information explicitly stated in the original problem.**
- Write only what is requested.

The story should be structured into **six paragraphs at most**, and follow this flow:

**Background → Rules and Problem Setting → Task Explanation → Examples and Closing**

Use the following genre: {GENRE}

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



"""
Please summarize the following text, which is a coding problem written in narrative story format. The goal is to make the text more concise while preserving the core explanation of the problem so that a reader can still produce the correct answer. 

### Guidelines for Summarization:

- Remove unnecessary parts of the narrative and retain only the essential elements required to understand the problem and write the correct solution. However, **the original narrative story format must be preserved.**
- You may keep the alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, **keep them in natural language only.**

The coding problem in narrative story format is as follows:

"""

SHORT_INSTRUCTION_CODEFORCES = """Please transform the coding problem into a brief narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.** Keep these descriptions **brief and unambiguous.**
- Build the story in given genre and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships. Avoid unnecessary elaboration and keep the world-building concise.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- You **must present the input and output format** as part of the story's narrative. If the input or output has multiple lines, your story must reflect this format accurately. Avoid vague phrases like “followed by”—instead, use clear terms like “on the next line” or “on the same line.”
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.
- Generate only what is requested.

The story should be short, concise, and structured into **three paragraphs at most**, and follow this flow:

**Rules and Problem Setting → Task Explanation → Examples and Closing**

Use the following genre: {GENRE}

The coding problem is as follows:

"""


SHORT_INSTRUCTION_LCB = """Please transform the coding problem into a brief narrative story format using the following guidelines.

### Guidelines for Narrative Conversion:

- You may use alphabetical symbols for quantity-related variables (such as N, M, K), and you may also use mathematical expressions (such as 10^5) when describing their constraints. However, all other variables must **not** be represented using symbols (such as ≤, ≥, =, or variable names); instead, describe them **indirectly through natural language only.** Keep these descriptions **brief and unambiguous.**
- Build the story in given genre and express each mathematical rule through **world-specific logic** such as social norms, systems, behaviors, or relationships. Avoid unnecessary elaboration and keep the world-building concise.
- You must include and **accurately reflect all original constraints and goals**, converting them into **clear symbolic analogies** within the narrative.
- Clearly convey that the goal is not just to meet the conditions, but to do so **as fully or efficiently as possible** within the world’s logic.
- Use **rich language** to build the world, but ensure that each rule remains **logically clear and inferable** to the reader. Don't get too caught up in narrative descriptions—focus on clearly explaining the problem as well.
- You **must present the input and output format** as part of the story's narrative. If the input or output has multiple lines, your story must reflect this format accurately. Avoid vague phrases like “followed by”—instead, use clear terms like “on the next line” or “on the same line.”
- Conclude the story by reframing all original sample inputs, outputs, and their explanations in the context of the narrative world.
- Write only what is requested.

The story should be short, concise, and structured into **three paragraphs at most**, and follow this flow:

**Rules and Problem Setting → Task Explanation → Examples and Closing**

Use the following genre: {GENRE}

The coding problem is as follows:

"""