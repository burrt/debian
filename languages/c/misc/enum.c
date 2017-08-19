#include <stdio.h>


enum Security_levels
{
    black_ops  = 4,
    top_secret = 3,
    secret     = 2,
    intern     = 1
};

const static char *str_sec_lvls[] = {
    "Black Ops",
    "Top Secret",
    "Secret",
    "Intern"
    };


int main(int argc, char **argv)
{
    enum Security_levels levels[4];
    levels[0] = black_ops;
    levels[1] = top_secret;
    levels[2] = secret;
    levels[3] = intern;

    printf("Security levels:\n");
    for (int i = 0; i < 4; i++)
        printf("* %s (%d)\n", str_sec_lvls[i], levels[i]);
    return 0;
}
