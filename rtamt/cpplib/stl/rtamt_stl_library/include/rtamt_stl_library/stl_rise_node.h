/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_rise.h
 * Author: nickovic
 *
 * Created on August 3, 2019, 5:23 PM
 */

#ifndef STL_RISE_H
#define STL_RISE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlRiseNode : public StlNode {
    private:
        double in;
        double prev_in;
        void addNewInput(int i, double msg);
        
        
    public:
        StlRiseNode();
        double update();
        void addNewInput(double msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_RISE_H */

