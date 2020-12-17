/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_eventually_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlEventuallyNode::StlEventuallyNode() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlEventuallyNode::reset() {
    prev_out = - std::numeric_limits<double>::infinity();
}

void StlEventuallyNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    in = sample;
}

void StlEventuallyNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlEventuallyNode::update() {
    double out;
    
    out = std::max(in, prev_out);
    prev_out = out;
    
    return out;
}