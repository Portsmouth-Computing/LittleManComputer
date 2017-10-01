#ifndef ASSEMBLER_H_INCLUDED
#define ASSEMBLER_H_INCLUDED

#include <string>
#include <vector>

class Assembler
{
    public:
        Assembler(const std::string& fileName);

        std::vector<uint16_t> assemble();

    private:
        std::vector<std::string> m_lines;

};

#endif // ASSEMBLER_H_INCLUDED
