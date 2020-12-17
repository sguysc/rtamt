/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_once_node.h
 * Author: nickovic
 *
 * Created on August 5, 2019, 10:09 PM
 */

#ifndef STL_ONCE_NODE_H
#define STL_ONCE_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>
#include <boost/circular_buffer.hpp>


namespace stl_library {

class StlOnceNode : public StlNode {
    private:
        double in;
        double prev_out;
        void addNewInput(int i, double msg);
        
        
    public:
        StlOnceNode();
        double update();
        void addNewInput(double msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ONCE_NODE_H */

