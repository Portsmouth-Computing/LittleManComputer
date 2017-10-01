#include "Assembler.h"

#include <fstream>
#include <unordered_map>

namespace
{
    const std::unordered_map<std::string, uint16_t> commands
    {
        { "HLT", 0},
        { "ADD", 1},
        { "SUB", 2},
        { "STA", 3},
        { "LDA", 5},
        { "BRA", 6},
        { "BRZ", 7},
        { "BRP", 8},
        { "INP", 9},
        { "OUT", 9},
        { "DAT", 4},
    }
}

Assembler::Assembler(const std::string& fileName)
{
    std::fstream inFile;
    std::string line;
    while (std::getline(inFile, line))
    {
        m_lines.push_back(line);
    }
}
