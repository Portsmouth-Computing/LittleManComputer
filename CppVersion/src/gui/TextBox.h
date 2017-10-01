#ifndef TEXTBOX_H_INCLUDED
#define TEXTBOX_H_INCLUDED

#include <SFML/Graphics.hpp>
#include <string>

class TextBox
{
    public:
        TextBox(float width, float height, int x, int y);

        void handleInput(sf::Event e);
        void draw       (sf::RenderWindow& window);

        const std::string& getText() const { return m_textBuffer; }

    private:
        sf::RectangleShape  m_box;
        sf::Font    m_font;
        sf::Text    m_text;
        std::string m_textBuffer;
};

#endif // TEXTBOX_H_INCLUDED
