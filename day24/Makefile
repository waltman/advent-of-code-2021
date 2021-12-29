C = /usr/bin/cc
CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
CPPFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
CPPOBJECTS = alu.o Odometer.o Monad.o timer.o

all: alu alu_test1 alu_test2 alu_test3

alu.o: Odometer.h Monad.h timer.h

alu_test1.o: Monad.h

alu_test2.o: Monad.h

alu_test3.o: Monad.h

Odometer.o: Odometer.h

Monad.o: Monad.h

timer.o: timer.h

%.o: %.cpp
	$(CPP) $(CPPFLAGS) -c $<

%.o: %.c
	$(C) $(CFLAGS) -c $<

alu: $(CPPOBJECTS)
	$(CPP) -o $@ $(CPPOBJECTS) $(LIBDIRS) $(LIBS)

alu_test1: alu_test1.o Monad.o
	$(CPP) -o $@ alu_test1.o Monad.o $(LIBDIRS) $(LIBS)

alu_test2: alu_test2.o Monad.o
	$(CPP) -o $@ alu_test2.o Monad.o $(LIBDIRS) $(LIBS)

alu_test3: alu_test3.o Monad.o
	$(CPP) -o $@ alu_test3.o Monad.o $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f alu alu_test1 alu_test2 alu_test3
