# 01-07-2026
- Towers can attack if enemies in range and enemies lose health
- Money increases when an enemy is killed
- Towers don't shoot every frame
- Adjust money worth per enemy type
- Towers can attack one enemy at a time
- Show enemy health

TODO:
- Add specific coordinates/square where you can build a tower
- clicking to select
- Create an enemy path that is not just a diagonal
- Introduce some randomness in enemy path
- Move level definitions and paths into a separate static file so different levels can store their own paths and enemy waves
- If enemy reaches the end of the display, Game over is shown

# 30-06-2026
- Collect cursor coordinates 
- add a menu where you can click to select tower to build

# 29-06-2026
- Created display with enemy path
- Towers now show up statically
- One enemy shows up and moves along the path
- Both enemies and towers appear as coloured circles
- Tower range appearing

# 26-06-2026
Enemies should have health, attack, move.

# Display:
## Enemies
Tank enemies should appear as "O|O" 
Flying enemies as "{|}" 
Weak enemies as "w|w"
Fast enemies as "(|)"

# Towers
Arrow tower: |H| and its attack symbol is "---"
Magic tower: |M| and its attack symbol is "www"
Artiller tower: |A| and its attack symbol is "O"
TODO later: create a wall/defender tower


