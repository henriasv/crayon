//
// plugin.cc
// pybind11 plugin to interface with relevant C++ codes
//
// Copyright (c) 2018 Wesley Reinhart.
// This file is part of the crayon project, released under the Modified BSD License.

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include "crayon.h"

#include "Neighborhood.h"
#include "Comparison.h"
#include "Neighbors.h"

PYBIND11_MODULE(_crayon, m)
    {
    m.doc() = "C++ bindings for crayon: a template-free crystal structure analysis";
    m.attr("__version__") = pybind11::make_tuple(CRAYON_VERSION_MAJOR, CRAYON_VERSION_MINOR, CRAYON_VERSION_PATCH);

        {
        using namespace crayon;

        // export to python via pybind11
        export_Neighborhood(m);
        export_Comparison(m);
        export_VoroNeighbors(m);

        } // end namespace crayon
    }
