C = /usr/bin/cc
CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
CPPFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
CPPOBJECTS = hydrothermal_venture.o

all: hydrothermal_venture

hydrothermal_venture.o: array2d.h

%.o: %.cpp
	$(CPP) $(CPPFLAGS) -c $<

%.o: %.c
	$(C) $(CFLAGS) -c $<

hydrothermal_venture: $(CPPOBJECTS)
	$(CPP) -o $@ $(CPPOBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f hydrothermal_venture
