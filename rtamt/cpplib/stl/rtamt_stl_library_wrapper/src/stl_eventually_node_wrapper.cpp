/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_eventually_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_eventually_node)
{
    class_<StlEventuallyNode, bases<StlNode> >("EventuallyOperation")
        .def("update", &StlEventuallyNode::update)
        .def("reset", &StlEventuallyNode::reset)
        .def("addNewInput", static_cast<void (StlEventuallyNode::*)(double)>(&StlEventuallyNode::addNewInput))
    ;
}