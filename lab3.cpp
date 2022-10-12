#include <GL/gl.h>
#include <bits/stdc++.h>
#include <GL/glut.h>

using namespace std;

struct point{
    float x,y;
    point(float a,float b){
        x=a,y=b;
    }
};

vector<point> v;

void draw(){
    glClear(GL_COLOR_BUFFER_BIT);
    glPointSize(10);
    glBegin(GL_POINTS);
    for(auto i : v){
        glColor3f(0,0,0);
        glVertex2f((GLfloat)round(i.x),(GLfloat)round(i.y));
    }
    glEnd();
    glFlush();
}

int main(int C, char* V[]){
    float x0,y0,xn,yn;
    int ch;
    cout<<"Select method:\n1.Bresenham\n2.Midpoint\n";
    cin>>ch;
    cout<<"Enter two points:\n";
    cin>>x0>>y0;//intial points
    cin>>xn>>yn; //final points
    vector<point> polynomial, dda;
    //Bresenham's Method
    if(ch==1){
    	float dx=abs(xn-x0), dy=abs(yn-y0);
		if(dx>=dy){
    		if(x0>xn){
    			swap(x0, xn);
    			swap(y0, yn);
    		}
    		v.push_back(point(x0, y0));
  			float x=x0, y=y0, p=(2*dy)-dx;
       		while(x<xn){
       			x++;
       			if(p>0){
       				y++;
       				p=p+2*(dy-dx);
       			}
       			else{
       				p=p+(2*dy);
       			}
       			v.push_back(point(x, y));
       		}
    	}
    	else{
    		if(y0>yn){
    			swap(x0, xn);
    			swap(y0, yn);
    		}
       		v.push_back(point(x0, y0));
  			float x=x0, y=y0, p=(2*dx)-dy;
       		while(y<yn){
       			y++;
       			if(p>0){
       				x++;
       				p=p+2*(dx-dy);
       			}
       			else{
       				p=p+(2*dx);
       			}
       			v.push_back(point(x, y));
       		}
    	}
    }
    // Midpoint Method
    else{
    	float dx=abs(xn-x0), dy=abs(yn-y0);
		if(dx>=dy){
    		if(x0>xn){
    			swap(x0, xn);
    			swap(y0, yn);
    		}
    		v.push_back(point(x0, y0));
  			float x=x0, y=y0, start=dy, end=-dx;
  			float d=start+(end/2);
       		while(x<xn){
       			x++;
       			if(d>0){
       				y++;
       				d=d+start+end;
       			}
       			else{
       				d=d+start;
       			}
       			v.push_back(point(x, y));
       		}
    	}
    	else{
    		if(y0>yn){
    			swap(x0, xn);
    			swap(y0, yn);
    		}
    		v.push_back(point(x0, y0));
  			float x=x0, y=y0, start=-dy, end=dx;
  			float d=(start/2)+end;
       		while(y<yn){
       			y++;
       			if(d>0){
       				x++;
       				d=d+start+end;
       			}
       			else{
       				d=d+end;
       			}
       			v.push_back(point(x, y));
       		}
    	}
    }
    glutInit(&C,V);
    glutInitWindowPosition(500,500);
    glutInitWindowSize(800,800);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutCreateWindow("sample");
    glClearColor(1,1,1,1);
    glutDisplayFunc(draw);
    gluOrtho2D(x0-50,xn+50,y0-50,yn+50);
    glutMainLoop();
}
