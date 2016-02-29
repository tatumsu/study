#include <unistd.h>
#include <signal.h>
 
static void hdl (int sig)
{
  
}
 
void my_sleep (int seconds)
{
  while (seconds > 0)
  {
    seconds = sleep (seconds);
    printf("Sleep is interrupted.\n");
  }
}
 
int main (int argc, char *argv[])
{
  // signal (SIGTERM, hdl);
  // signal (SIGINT, hdl);

  my_sleep (10);
 
  return 0;
}
