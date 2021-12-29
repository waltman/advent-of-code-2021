// -*- mode: c++; -*-
// DESCRIPTION: main module for Timer class
//
// Copyright(C) 1/24/2008 by Walt Mankowski
// walt@cs.drexel.edu
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
// $Id: timer.cpp 163 2008-02-17 19:51:24Z walt $

#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <time.h>
#include "timer.h"

/*******************************************************************************
** Method Name: die
**
** Parameters: char *fmt, ...
**
** Description: Print a warning to stderr and exit.  Format is the same as
**              printf().  It errno is set, it's converted to an error string
**              and printed.
**
** Returns: Sets exit status to errno upon exiting.
**
*******************************************************************************/
void Timer::die(const char *fmt, ...) {
        int save_errno = errno;

        va_list ap;

        va_start(ap, fmt);
        vfprintf(stderr, fmt, ap);
        va_end(ap);

        if (save_errno)
                fprintf(stderr, ": %s", strerror(save_errno));

        fprintf(stderr, "\n");

        exit(save_errno);
}

/*******************************************************************************
** Method Name: Timer constructor
**
** Parameters: none
**
** Description: Clears all the instance variables
**
** Returns: n/a
**
*******************************************************************************/
Timer::Timer() {
        timerclear(&start_utime);
        timerclear(&start_stime);
        timerclear(&start_wtime);
        timerclear(&stop_utime);
        timerclear(&stop_stime);
        timerclear(&stop_wtime);
}

/*******************************************************************************
** Method Name: start
**
** Parameters: none
**
** Description: Sets the timer, setting the appropriate instance variables
**              to the current time.
**
** Returns: void
**
*******************************************************************************/
void Timer::start() {
        struct rusage usage;

        if (getrusage(RUSAGE_SELF, &usage) != 0)
                die("calling getrusage() in Timer::start()");

        start_utime = usage.ru_utime;
        start_stime = usage.ru_stime;

        // get starting wall time
        gettimeofday(&start_wtime, NULL);
}

/*******************************************************************************
** Method Name: stop
**
** Parameters: none
**
** Description: Stops the timer, setting the appropriate instance variables
**              to the current time.
**
** Returns: void
**
*******************************************************************************/
void Timer::stop() {
        struct rusage usage;

        if (getrusage(RUSAGE_SELF, &usage) != 0)
                die("calling getrusage() in Timer::stop()");

        stop_utime = usage.ru_utime;
        stop_stime = usage.ru_stime;

        // get ending wall time
        gettimeofday(&stop_wtime, NULL);
}

/*******************************************************************************
** Method Name: delta_tv
**
** Parameters: const struct timeval *a, const struct timeval *b
**
** Description: returns the difference between timevals a and b as a double
**
** Returns: the difference in seconds between a and b
**
*******************************************************************************/
double Timer::delta_tv(const struct timeval *a, const struct timeval *b) const {
        struct timeval delta;;

        timersub(b, a, &delta);
        return tv2double(&delta);
}

/*******************************************************************************
** Method Name: tv2double
**
** Parameters: const struct timeval *tv
**
** Description: converts a timeval into a double
**
** Returns: the structure's representation as a double
**
*******************************************************************************/
double Timer::tv2double(const struct timeval *tv) const {
        return tv->tv_sec + tv->tv_usec / 1e6;
}
