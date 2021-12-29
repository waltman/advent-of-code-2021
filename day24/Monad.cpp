#include <ctype.h>
#include <string.h>
#include <string>
#include "Monad.h"

Monad::Monad(int *input) {
    reset(input);
}

void Monad::reset(int *input = NULL) {
    if (input != NULL)
        _input = input;

    inp_ptr = 0;
    memset(reg, 0, sizeof(reg));
}
    

void Monad::add_cmd(const string cmd) {
    char cmd_str[20];
    char *tok;
    struct cmd command;
    memset(&command, 0, sizeof(command));
    
    strcpy(cmd_str, cmd.c_str());

    // get the op
    tok = strtok(cmd_str, " ");

    command.a = cmd_str[4];
    if (strcmp(tok, "inp") == 0) {
        command.op = 0;
    } else {
        if (strcmp(tok, "add") == 0)
            command.op = 1;
        else if (strcmp(tok, "mul") == 0)
            command.op = 2;
        else if (strcmp(tok, "div") == 0)
            command.op = 3;
        else if (strcmp(tok, "mod") == 0)
            command.op = 4;
        else if (strcmp(tok, "eql") == 0)
            command.op = 5;

        // skip the next token since we already have it
        strtok(NULL, " ");

        // the final token is either a char or a number
        tok = strtok(NULL, " ");
        if (tok[0] >= 'w' and tok[0] <= 'z') {
            command.b_k = tok[0];
            command.constant = false;
        } else {
            command.b_val = atoll(tok);
            command.constant = true;
        }
    }
    _pgm.push_back(command);
}

void Monad::run_cmd(struct cmd command) {
    int a = command.a - 'w';
    if (command.op == 0)
        reg[a] = _input[inp_ptr++];
    else {
        long long val = command.constant ? command.b_val : reg[command.b_k - 'w'];
        switch (command.op) {
        case 1:
            reg[a] += val;
            break;
        case 2:
            reg[a] *= val;
            break;
        case 3:
            reg[a] /= val;
            break;
        case 4:
            reg[a] %= val;
            break;
        case 5:
            reg[a] = (reg[a] == val) ? 1 : 0;
            break;
        }
    }
}

void Monad::run() {
    for (auto command : _pgm)
        run_cmd(command);
}
