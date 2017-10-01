#ifndef LITTLEMANCOMPUTER_H_INCLUDED
#define LITTLEMANCOMPUTER_H_INCLUDED

#include <SFML/Graphics.hpp>

class LittleManComputer
{
    public:
        LittleManComputer();

        void boot();

    private:
        void handleWindowEvents();

        sf::RenderWindow m_window;
};

#endif // LITTLEMANCOMPUTER_H_INCLUDED
