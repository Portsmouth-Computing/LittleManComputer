#include "TextBox.h"

#include "../Utilities.h"

enum Key
{
    BackSpace = 8,
};

TextBox::TextBox(float width, float height, int x, int y)
{
    m_box.setPosition   ( x,        y);
    m_box.setSize       ({width,    height});

    m_font.loadFromFile("res/PTM55FT.ttf");
    m_text.setFont(m_font);
}

void TextBox::handleInput(sf::Event e)
{
    if (e.type == sf::Event::TextEntered)
    {

        auto keyCode = e.text.unicode;


        if (isInclusiveRange(keyCode, 32, 127))
        {
            m_textBuffer.push_back(keyCode);
        }
        else if (keyCode == Key::BackSpace)
        {
            if (!m_textBuffer.empty())
            {
                m_textBuffer.pop_back();
            }
        }

    }
}

void TextBox::draw(sf::RenderWindow& window)
{

}
