// -*- mode: c++; -*-
// DESCRIPTION: Header file for Timer class
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
// $Id: timer.h 163 2008-02-17 19:51:24Z walt $

#ifndef _TIMER_H
#define _TIMER_H

#include <sys/time.h>
#include <sys/resource.h>

// Simple object that functions like a stopwatch to get elapsed
// system, user, and wall time.  Call the start() method to set the
// timer, stop() to stop it.  You can then query the values with
// utime() stime(), and wtime().
//
// This is mainly a wrapper to convert the struct timeval's into
// doubles so the caller doesn't have to worry about them.


class Timer {
private:
        struct timeval start_utime;
        struct timeval start_stime;
        struct timeval start_wtime;
        struct timeval stop_utime;
        struct timeval stop_stime;
        struct timeval stop_wtime;

        void die(const char *fmt, ...);
        double delta_tv(const struct timeval *a, const struct timeval *b) const;
        double tv2double(const struct timeval *tv) const;

public:
        Timer();
        ~Timer() {}
        void start();
        void stop();
        double utime() const { return delta_tv(&start_utime, &stop_utime); }
        double stime() const { return delta_tv(&start_stime, &stop_stime); }
        double wtime() const { return delta_tv(&start_wtime, &stop_wtime); }
};

#endif
