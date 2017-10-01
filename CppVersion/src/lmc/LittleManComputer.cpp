#include "LittleManComputer.h"

LittleManComputer::LittleManComputer()
:   m_window({1280, 720}, "LittleManComputer")
{

}

void LittleManComputer::boot()
{
    while (m_window.isOpen())
    {
        m_window.clear();


        m_window.display();
        handleWindowEvents();
    }
}

void LittleManComputer::handleWindowEvents()
{
    sf::Event e;
    while (m_window.pollEvent(e))
    {
        switch(e.type)
        {
            case sf::Event::Closed:
                m_window.close();
                break;

            default:
                break;
        }
    }
}
