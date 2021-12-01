CPP = /usr/bin/c++
INCLDIRS =
LIBDIRS =
LIBS =
CFLAGS = -std=c++17 -Wall -O3 $(INCLDIRS)
OBJECTS = sonar_sweep.o

all: sonar_sweep

%.o: %.cpp
	$(CPP) $(CFLAGS) -c $<

sonar_sweep: $(OBJECTS)
	$(CPP) -o $@ $(OBJECTS) $(LIBDIRS) $(LIBS)

clean:
	rm -f *~
	rm -f *.o
	rm -f sonar_sweep
