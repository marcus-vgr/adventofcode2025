#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

class Day9{

    public:
        Day9(std::string filename);
        std::vector<int> xvalues, yvalues;
        std::vector<int> unique;

        unsigned long long solution1();
        unsigned long long solution2();
    
    private:
        void readInput(std::string filename);
        void makeCoordinateCompression();
        std::vector<std::pair<std::vector<int>,unsigned long long>> getAllRetangles();
        std::vector<std::vector<bool>> createGridLights();

};

Day9::Day9(std::string filename){
    readInput(filename);
    makeCoordinateCompression();
}

void Day9::readInput(std::string filename){

    std::ifstream file(filename);

    int x,y;
    char comma;

    while(file >> x >> comma >> y){
        xvalues.push_back(x);
        yvalues.push_back(y);
    }

}

void Day9::makeCoordinateCompression(){

    std::vector<int> allValues = xvalues;
    allValues.insert(allValues.end(), yvalues.begin(), yvalues.end());

    std::sort(allValues.begin(), allValues.end());

    unique.push_back(allValues[0]);
    for(int i = 1; i < allValues.size(); i++){
        if (allValues[i] != allValues[i-1]) unique.push_back(allValues[i]);
    }

    std::map<int,int> replace; 
    for(int i = 0; i < unique.size(); i++){
        replace[unique[i]] = i;
    }

    for(int i = 0; i < xvalues.size(); i++){
        xvalues[i] = replace[xvalues[i]];
        yvalues[i] = replace[yvalues[i]];
    }

}

std::vector<std::pair<std::vector<int>,unsigned long long>> Day9::getAllRetangles(){
    int N = xvalues.size();
    std::vector<std::pair<std::vector<int>,unsigned long long>> retangles;

    int x1,x2,y1,y2;
    unsigned long long area;
    for(int i = 0; i < N-1; i++){
        for(int j = i+1; j < N; j++){
            x1 = xvalues[i];
            y1 = yvalues[i];
            x2 = xvalues[j];
            y2 = yvalues[j];

            unsigned long long dx = static_cast<unsigned long long> (abs(unique[x1] - unique[x2]) + 1);
            unsigned long long dy = static_cast<unsigned long long> (abs(unique[y1] - unique[y2]) + 1);
            // make this otherwise the multiplication assuming unique is vector<int> will lead to overflow!!
            area = dx * dy;
            
            retangles.emplace_back(
                std::vector<int>{x1,y1,x2,y2},area
            );
        }
    }

    std::sort(retangles.begin(), retangles.end(), 
    [](std::pair<std::vector<int>,unsigned long long> a, std::pair<std::vector<int>,unsigned long long> b){
        return a.second > b.second;
    }
    );

    return retangles;
}

std::vector<std::vector<bool>> Day9::createGridLights(){

    int maxX = *std::max_element(xvalues.begin(), xvalues.end());
    int maxY = *std::max_element(yvalues.begin(), yvalues.end()); 
    std::vector<std::vector<bool>> grid(maxY+1, std::vector<bool>(maxX+1, 0));
    

    int N = xvalues.size();
    int x1, y1, x2, y2;
    
    // RedLights
    for(int i = 0; i < N; i++){
        x1 = xvalues[i];
        y1 = yvalues[i];
        grid[y1][x1] = 1;
    }

    
    // Border GreenLights
    for(int i = 0; i < N-1; i++){
        for(int j = i+1; j < N; j++){
            x1 = xvalues[i];
            y1 = yvalues[i];
            x2 = xvalues[j];
            y2 = yvalues[j];
            if(x1 > x2) std::swap(x1,x2);
            if(y1 > y2) std::swap(y1,y2);

            if(y1 == y2){
                for(int k = x1; k < x2+1; k++){
                    grid[y1][k] = 1;
                }
            }
            if(x1 == x2){
                for(int k = y1; k < y2+1; k++){
                    grid[k][x1] = 1;
                }
            }
        }
    }

    // Fill lights inside
    for(int i = 0; i < maxY+1; i++){
        std::vector<int> borders;
        for(int j = 0; j < maxX+1; j++){
            if(grid[i][j] == 1) borders.push_back(j);
        }
        int nBorders = borders.size();
        if(nBorders > 1){
            for(int k = borders[0]; k < borders[nBorders-1]+1; k++){
                grid[i][k] = 1;
            }
        }
    }
    
    return grid;
}

unsigned long long Day9::solution1(){

    auto retangles = getAllRetangles();
    
    return retangles[0].second;
}

unsigned long long Day9::solution2(){

    auto retangles = getAllRetangles();
    auto grid = createGridLights();

    int x1,x2,y1,y2;
    for(auto &[coords, area]: retangles){
        x1 = coords[0];
        y1 = coords[1];
        x2 = coords[2];
        y2 = coords[3];
        if(x1 > x2) std::swap(x1, x2);
        if(y1 > y2) std::swap(y1, y2);

        bool fails = false;
        for(int y = y1; y < y2+1; y++){
            fails = std::find(
                grid[y].begin()+x1, grid[y].begin()+x2+1, 0
            ) != grid[y].begin()+x2+1;

            if(fails) break;
        }

        if(!fails) return area; 

    }

    return 0;
}



int main(){

    Day9 test("test.txt");
    std::cout << test.solution2() << std::endl;

    Day9 final("input.txt");
    std::cout << final.solution2() << std::endl;

    return 0;
}