C = /usr/bin/cc
CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
CPPFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
CPPOBJECTS = alu.o Odometer.o Monad.o

all: alu

alu.o: Odometer.h Monad.h

Odometer.o: Odometer.h

Monad.o: Monad.h

%.o: %.cpp
	$(CPP) $(CPPFLAGS) -c $<

%.o: %.c
	$(C) $(CFLAGS) -c $<

alu: $(CPPOBJECTS)
	$(CPP) -o $@ $(CPPOBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f alu
