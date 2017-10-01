#include <iostream>
#include <SFML/Graphics.hpp>

void handleWindowEvents(sf::RenderWindow& window)
{
    sf::Event e;
    while (window.pollEvent(e))
    {
        switch(e.type)
        {
            case sf::Event::Closed:
                window.close();
                break;

            default:
                break;
        }
    }
}

int main()
{
    sf::RenderWindow window({1280, 720}, "LittleManComputer");

    while (window.isOpen())
    {
        window.clear();


        window.display();
        handleWindowEvents(window);
    }


}
