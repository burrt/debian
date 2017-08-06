#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include <ctype.h>


static char* commandhelp =
    "Usage: argparser [OPTION] ...\n\n"
    "  -n          stores integer value into variable\n"
    "  -s          stores string value into varible\n"
    "  -h          print the help information\n"
    "  -v          print version information\n\n"
    "An example of using getopt for arguments.\n"
    "getopt does not support long commands e.g. --option.";


int main (int argc, char** argv)
{
    int c;
    opterr = 0;

    // If no options
    if (argc == 1)
    {
        printf("%s\n", commandhelp);
        return 0;
    }
    while (optind < argc)
    {
        // :  required argument
        // :: optional argument
        if ((c = getopt(argc, argv, "h::n:s:v::")) != -1)
        {
            switch (c)
            {
            case 'h':
              printf("%s\n", commandhelp);
              break;
            case 'n':
              printf("Number: %d\n", atoi(optarg));
              break;
            case 's':
              printf("String: %s\n", optarg);
              break;
            case 'v':
              printf("Version 1.0\n");
              break;
            // If option was specified but no succeeding arguement, print error
            case '?':
              if (optopt == 'n')
                fprintf (stderr, "Option -%c requires an integer argument.\n", optopt);
              else if (optopt == 's')
                fprintf (stderr, "Option -%c requires a string argument.\n", optopt);
              else if (isprint (optopt))
                fprintf (stderr, "Unknown option `-%c'.\n", optopt);
              else
                fprintf (stderr, "Unknown option character `\\x%x'.\n", optopt);
              return 0;
            default:
                printf("No arguments to pass\n");
                return 0;
            }
        }
        else
        {
            printf("%s\n", commandhelp);
            return 0;
        }
    }
}
