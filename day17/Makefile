C = /usr/bin/cc
CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -Wall -O3 $(INCLDIRS)
CPPFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
CPPOBJECTS = trick_shot.o

all: trick_shot

%.o: %.cpp
	$(CPP) $(CPPFLAGS) -c $<

%.o: %.c
	$(C) $(CFLAGS) -c $<

trick_shot: $(CPPOBJECTS)
	$(CPP) -o $@ $(CPPOBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f trick_shot
